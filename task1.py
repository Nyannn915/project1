def calculate_value(board):
    result = 0
    for row in board:
        for letter in row:
            if letter in ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U']:
                result = result + 1
            elif letter in ['D', 'G']:
                result = result + 2
            elif letter in ['B', 'C', 'M', 'P']:
                result = result + 3
            elif letter in ['F', 'H', 'V', 'W', 'Y']:
                result = result + 4
            elif letter == 'K':
                result = result + 5
            elif letter in ['J', 'X']:
                result = result + 8
            elif letter in ['Q', 'Z']:
                result = result + 10
            else:
                result = result + 0
    return result

# 测试
print(calculate_value([["A"]]))         
print(calculate_value([["Z"]]))         
