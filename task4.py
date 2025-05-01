def textoggle_move(board, word_sequence, spare_letters):
    new_board = []
    for i in range(len(board)):
        new_row = []
        for j in range(len(board[i])):
            new_row.append(board[i][j])
        new_board.append(new_row)
    
    for position in word_sequence:
        row_index = position[0]
        col_index = position[1]
        new_board[row_index][col_index] = None
    
    return new_board
