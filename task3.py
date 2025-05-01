def find_word(w, b):
    n = len(b)
    m = len(b[0])
    
    def dfs(x, y, idx, vis, steps):
        if idx == len(w):
            return steps[:]
        if x < 0 or x >= n or y < 0 or y >= m:
            return None
        if (x, y) in vis:
            return None
        if b[x][y] != w[idx]:
            return None
        
        vis.add((x, y))
        steps.append((x, y))
        
        up = dfs(x - 1, y, idx + 1, vis, steps)
        if up:
            return up
        down = dfs(x + 1, y, idx + 1, vis, steps)
        if down:
            return down
        left = dfs(x, y - 1, idx + 1, vis, steps)
        if left:
            return left
        right = dfs(x, y + 1, idx + 1, vis, steps)
        if right:
            return right
        
        steps.pop()
        vis.remove((x, y))
        return None
    
    for i in range(n):
        for j in range(m):
            visited_set = set()
            path_list = []
            result = dfs(i, j, 0, visited_set, path_list)
            if result:
                return result
    return None

#测试代码 
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

test_words = [
    "SFCB",    
    "ADEE",    
]

for word in test_words:
    print(f"查找单词: {word}")
    path = find_word(word, board)
    if path:
        print(f"  找到了！路径是: {path}")
    else:
        print(f"  没找到。")
    print("-" * 35)