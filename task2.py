def words_on_board(words, board):
    # blank tile处理思路参考自Stackoom（https://stackoom.com/en/question/3Dz3N）
    tiles = []
    for line in board:
        for tile in line:
            tiles.append(tile)
    
    result = []
    for word in words:
        hand = tiles.copy()
        valid = True
        for letter in word:
            if letter in hand:
                hand.remove(letter)
            elif '_' in hand:
                hand.remove('_')
            else:
                valid = False
                break
        if valid:
            result.append(word)
    return result

