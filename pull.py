import random
import Database as DB
import A_TO_Z_range
choose_letter_index = random.randint(1, 26)  
#choose_word = random.randint(0, 4158)        


def word_label():
    word_instance = DB.Word()
    A_TO_Z = word_instance.change_number_to_word()
    
    dir_for_word = {}
    for i in range(len(A_TO_Z)):
        dir_for_word[i + 1] = A_TO_Z[i]  # {1: 'a', 2: 'b', ..., 26: 'z'}
        
    return dir_for_word


word_for_random = word_label()
Data_all = c.sent()  

# Retrieve the chosen letter and word
if choose_letter_index in word_for_random:      # number in number random
    letter = word_for_random[choose_letter_index] # e.g., 'c'

    start, end = A_TO_Z_range.get_range(letter)
    
    choose_word = random.randint(start, end - 1)
    
    if letter in Data_all: # {'a': {0:(word, tran), 1:(word, tran)......}}
        words_for_letter = Data_all[letter] # 0-4158  number get {0,(word, tran)}
        
        if choose_word in words_for_letter: # random same range
            question = words_for_letter[choose_word][0]
            answer = words_for_letter[choose_word][1]
            print("Question:", question)
            print("Answer:", answer)
        else:
            print(f"Fuck you ไม่ต้องทำ")
    else:
        print(f"not found word")
else:
    print("out range")