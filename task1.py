def calculate_value(board):
    # 试试能不能把所有字母和分数提前写成字典
    score_dict = {
        'Q': 10, 'q': 10, 'J': 8, 'j': 8, 'Z': 10, 'z': 10, 'X': 8, 'x': 8,
        'B': 3, 'b': 3, 'C': 3, 'c': 3, 'M': 3, 'm': 3, 'P': 3, 'p': 3,
        'D': 2, 'd': 2, 'G': 2, 'g': 2,
        'F': 4, 'f': 4, 'H': 4, 'h': 4, 'V': 4, 'v': 4, 'W': 4, 'w': 4, 'Y': 4, 'y': 4,
        'E': 1, 'e': 1, 'A': 1, 'a': 1, 'I': 1, 'i': 1, 'O': 1, 'o': 1,
        'N': 1, 'n': 1, 'R': 1, 'r': 1, 'T': 1, 't': 1, 'L': 1, 'l': 1, 'S': 1, 's': 1, 'U': 1, 'u': 1,
        'K': 5, 'k': 5
    }
    total = 0
    for row in board:
        for letter in row:
            total = total + score_dict.get(letter, 0)  # 如果不在字典里的话就加0分
    return total

# 测试一下
print(calculate_value([["a", "G"], ["C", "k"]])) 
print(calculate_value([["Q", "z"], ["?", "l"]]))  