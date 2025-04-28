def words_on_board(words, board):
    tiles_list = []
    
    for row_number in range(len(board)):
        current_row = board[row_number]
        
       
        for tile_number in range(len(current_row)):
            
            tiles_list.append(current_row[tile_number])
    
    valid_words = []
    
    for word_index in range(len(words)):
        
        current_word = words[word_index]
        
        hand_copy = []
        for i in range(len(tiles_list)):
            hand_copy.append(tiles_list[i])
        
        is_valid = True
        
        for letter_position in range(len(current_word)):
            
            current_letter = current_word[letter_position]
            
            found_in_hand = False
            for j in range(len(hand_copy)):
                if hand_copy[j] == current_letter:
                    
                    hand_copy.pop(j)
                    found_in_hand = True
                    break
            
            
            if not found_in_hand:
                is_valid = False
                break
        
        
        if is_valid:
            valid_words.append(current_word)
    
    return valid_words



# board = [
#         ['A', 'B', 'C'],
#         ['D', 'E', 'F']
#     ]
# words = ['AB', 'FACE', 'BED', 'BAD', 'FED', 'CAB', 'ACE']

# result = words_on_board(words, board)
# print("测试结果：", result)