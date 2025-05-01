def find_word(w, b):
  
    n = len(b)
    m = len(b[0])
    for r in range(n):
        for c in range(m):
            k = 0
            x, y = r, c
            while k < len(w):
                if x >= n:  
                    break
                if b[x][y] != w[k]:
                    break
                k += 1
                x += 1
            if k == len(w):
                return True
    return False