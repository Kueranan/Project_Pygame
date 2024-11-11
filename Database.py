import pandas as pd
import os
import json


df_1 = pd.read_csv('data_word_thai_eng.csv')

class Word:
    def __init__(self):
        self.A_TO_Z = []
    
    def change_number_to_word(self):
        for i in range(26):
            self.A_TO_Z.append(chr(97 + i))
        return self.A_TO_Z

class SplitWordByLetter:
    def __init__(self, letters):
        self.letters = letters
        self.dir_word = {letter: {} for letter in letters}  # {'a' : {}..... 'z': {}}
    
    def add_to_dict(self, words, translations):
        for index, (word, translation) in enumerate(zip(words, translations)):
            if isinstance(word, str) and word:  
                first_letter = word[0].lower()  # check char a-z
                if first_letter in self.dir_word:
                    self.dir_word[first_letter][index] = (word, translation)   #{'a' : {0 : (word, tran)}} 
                else:
                    return 'Not thing in A-Z'
            else:
                return 'word not in row'
        return self.dir_word



    
def sent():
    word_instance = Word()
    A_TO_Z = word_instance.change_number_to_word()
    splitter = SplitWordByLetter(A_TO_Z)
    result = splitter.add_to_dict(df_1['e-search'], df_1['t-entry'])
    return result

#print(sent())
    
        
