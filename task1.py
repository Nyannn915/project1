def calculate_value(board):
    # Set letter scores
    scores = {
        **dict.fromkeys(['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U'], 1),
        **dict.fromkeys(['D', 'G'], 2),
        **dict.fromkeys(['B', 'C', 'M', 'P'], 3),
        **dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4),
        'K': 5,
        **dict.fromkeys(['J', 'X'], 8),
        **dict.fromkeys(['Q', 'Z'], 10),
    }
    
    total = 0  # Total score
    for row in board:
        for letter in row:
            total += scores.get(letter, 0)  
    return total


print(calculate_value([["A", "G"], ["C", "k"]]))  
print(calculate_value([["Q", "z"], ["?", "L"]]))  