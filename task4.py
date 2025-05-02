def textoggle_move(board, word_sequence, spare_letters):
    new_board = [row[:] for row in board]

    for row, col in word_sequence:
        new_board[row][col] = None

    height = len(board)
    width = len(board[0])
    spare_index = 0  

    for col in range(width):
        remaining = []

        for row in range(height - 1, -1, -1):
            if new_board[row][col] is not None:
                remaining.append(new_board[row][col])

        for row in range(height - 1, -1, -1):
            if remaining:
                new_board[row][col] = remaining.pop(0)
            elif spare_index < len(spare_letters):
                new_board[row][col] = spare_letters[spare_index]
                spare_index += 1
            else:
                new_board[row][col] = '#'  

    return new_board




new_board = textoggle_move([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], [(1, 0), (0, 0), (0, 1)], ['Q', 'R'])
[['R', '#', 'C'], ['Q', 'E', 'F'], ['G', 'H', 'I']] 

print("textoggle_move：")
for row in new_board:
    print(row)