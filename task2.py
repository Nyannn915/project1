def words_on_board(words, board):
    all_tiles = []
    for row in board:
        for letter in row:
            all_tiles.append(letter)

    tile_counter = Counter()
    for ch in all_tiles:
        tile_counter[ch] += 1

    result = []
    for word in words:
        word_counter = Counter()
        for c in word:
            word_counter[c] += 1

        ok = True
        used_blanks = 0 

        for ch in word_counter:
            if ch in tile_counter:
                
                if tile_counter[ch] >= word_counter[ch]:
                    continue
                else:
                    blanks = tile_counter.get('_', 0) - used_blanks
                    left_need = word_counter[ch] - tile_counter[ch]
                    if blanks >= left_need:
                        used_blanks += left_need
                    else:
                        ok = False
                        break
            else:
