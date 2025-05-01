def word_on_board(word, board):
    height = len(board)
    width = len(board[0])
    
    for row in range(height):
        for col in range(width):
            if board[row][col] != word[0]:
                continue  
                
            visited = set()
            steps = []
            
            visited.add((row, col))
            steps.append((row, col))
            
            if search_remaining(word, 1, row, col, board, visited, steps):
                return steps  
    
    return None  


def search_remaining(word, index, row, col, board, visited, steps):
    if index >= len(word):
        return True
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for direction in directions:
        dr, dc = direction
        r = row + dr
        c = col + dc
        
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            continue  
            
        if (r, c) in visited:
            continue
            
        if board[r][c] != word[index]:
            continue
            
        visited.add((r, c))
        steps.append((r, c))
        
        if search_remaining(word, index + 1, r, c, board, visited, steps):
            return True
            
        visited.remove((r, c))
        steps.pop()
    
    return False