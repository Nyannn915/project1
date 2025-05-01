def find_word(word, board):
    n = len(board)
    m = len(board[0])
    
    def search(x, y, idx, visited):
        if idx == len(word):
            return True
        
        if x < 0 or x >= n:
            return False
        if y < 0 or y >= m:
            return False
        
        if (x, y) in visited:
            return False
        
        if board[x][y] != word[idx]:
            return False
        
        visited.add((x, y))
        
        right = search(x + 1, y, idx + 1, visited)
        if right:
            visited.remove((x, y))
            return True
        
        left = search(x - 1, y, idx + 1, visited)
        if left:
            visited.remove((x, y))
            return True
        
        down = search(x, y + 1, idx + 1, visited)
        if down:
            visited.remove((x, y))
            return True
        
        up = search(x, y - 1, idx + 1, visited)
        if up:
            visited.remove((x, y))
            return True
        
        visited.remove((x, y))
        return False
    
    for i in range(n):
        for j in range(m):
            visited = set()
            if search(i, j, 0, visited):
                print(f"找到了，单词'{word}'起点在({i},{j})。")
                return True
    
    print(f"没找到单词'{word}'。")
    return False

# 测试代码
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

for word in ['CAT', 'DOG', 'PIG', 'COP']:
    find_word(word, board)