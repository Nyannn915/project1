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
        
        row_index = height - 1
        while row_index >= 0:
            if new_board[row_index][col] is not None:
                stack.append(new_board[row_index][col])
            row_index -= 1
        
        
        row_index = height - 1
        while row_index >= 0:
            if stack:
                new_board[row_index][col] = stack.pop(0)
            else:
                new_board[row_index][col] = None
            row_index -= 1
        
        column_result = []
        for r in range(height):
            column_result.append(new_board[r][col])   
    return new_board