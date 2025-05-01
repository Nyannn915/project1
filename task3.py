def word_on_board(word, board):
    height = len(board)
    width = len(board[0])
    for row in range(height):
        for col in range(board[0]):
            steps = [(row, col)]
            visited = {(row, col)}
            if search(word, 1, row, col, board, visited, steps):
                return steps
    return None

def search(word, index, row, col, board, visited, steps):
    if index == len(word):
        return True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    height, width = len(board), len(board[0])
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if (0 <= r < rows and 0 <= c < cols and (r, c) not in visited and board[r][c] == word[index]):
            visited.add((r, c))
            steps.append((r, c))
            if search(word, index + 1, r, c, board, visited, steps):
                return True
            visited.remove((r, c))
            steps.pop()
    return False
