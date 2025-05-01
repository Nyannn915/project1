# firstly, use function to check if a given word exists on the board as a valid path
def word_on_board(word, board):
    height = len(board)
    width = len(board[0])

    # try every cell on the board as a starting point
    for row in range(height):
        for col in range(width):
            # if the current cell matches the first character of the word
            if board[row][col] == word[0]:
                steps = [(row, col)]  # store path as list of positions
                visited = {(row, col)}  # mark the starting cell as visited

                # perform recursive search from this position
                if search(
                    word,
                    1,
                    row,
                    col,
                    board,
                    visited,
                    steps
                ):
                    return steps  # return path if successful

    # return None if the word cannot be found
    return None


# keeps checking the rest of the letters one by one from here
def search(word, index, row, col, board, visited, steps):
    # if we've already matched all the letters, we're done
    if index == len(word):
        return True

    # check the four directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    height = len(board)
    width = len(board[0])

    # try each direction from the current position
    for dr, dc in directions:
        r = row + dr
        c = col + dc

        # check bounds, not visited, and matches next letter in word
        if (
            0 <= r < height
            and 0 <= c < width
            and (r, c) not in visited
            and board[r][c] == word[index]
        ):
            visited.add((r, c))      # mark as visited
            steps.append((r, c))     # add to path

            # keep checking the next letter from here
            if search(
                word,
                index + 1,
                r,
                c,
                board,
                visited,
                steps
            ):
                return True

            # backtrack if search fails: unvisit and remove from path
            visited.remove((r, c))
            steps.pop()

    # if no direction leads to solution, return False
    return False
