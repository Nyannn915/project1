def calculate_value(board):
    sum_score = 0
    for row in board:
        for letter in row:
            if letter in ['E', 'e', 'A', 'a', 'I', 'i', 'O', 'o', 'N', 'n', 'R', 'r', 'T', 't', 'L', 'l', 'S', 's', 'U', 'u']:
                sum_score = sum_score + 1
            elif letter in ['D', 'd', 'G', 'g']:
                sum_score = sum_score + 2
            elif letter in ['B', 'b', 'C', 'c', 'M', 'm', 'P', 'p']:
                sum_score = sum_score + 3
            elif letter in ['F', 'f', 'H', 'h', 'V', 'v', 'W', 'w', 'Y', 'y']:
                sum_score = sum_score + 4
            elif letter in ['K', 'k']:
                sum_score = sum_score + 5
            elif letter in ['J', 'j', 'X', 'x']:
                sum_score = sum_score + 8
            elif letter in ['Q', 'q', 'Z', 'z']:
                sum_score = sum_score + 10
            else:
                sum_score = sum_score + 0
    return sum_score

print(calculate_value([["Z", "E"]])) 
print(calculate_value([["?", " "], ["1", "A"]]))