def textoggle_move(board, word_sequence, spare_letters):
    new_board = []
    for i in range(len(board)):
        new_row = []
        for j in range(len(board[i])):
            
            new_row.append(board[i][j])
        
        new_board.append(new_row)
    
    
    return new_board