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
    
    height = len(board)
    width = len(board[0])
    
    for col in range(width):
        stack = []
        
        for row in range(height-1, -1, -1):
            if new_board[row][col] is not None:
                stack.append(new_board[row][col])
        
        for row in range(height-1, -1, -1):
            if stack:
                new_board[row][col] = stack.pop(0)
            else:
                if spare_letters:
                    new_board[row][col] = spare_letters[0]
                else:
                    new_board[row][col] = None
    
    return new_board