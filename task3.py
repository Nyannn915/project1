def find_word(w, b):
    n = len(b)
    m = len(b[0])
    for r in range(n):
        for c in range(m):
            # 检查向下
            k = 0
            x = r
            y = c
            while k < len(w):
                if x >= n or b[x][y] != w[k]:
                    break
                k += 1
                x += 1
            if k == len(w):
                return True

            # 检查向右
            kk = 0
            xx = r
            yy = c
            while kk < len(w):
                if yy >= m or b[xx][yy] != w[kk]:
                    break
                kk += 1
                yy += 1
            if kk == len(w):
                
                return True

    
    return False

# 简单测试
board = [
    ['C', 'A', 'T'],
    ['D', 'O', 'G'],
    ['P', 'I', 'G']
]

for word in ['CAT', 'DOG', 'PIG', 'COP']:
    find_word(word, board)