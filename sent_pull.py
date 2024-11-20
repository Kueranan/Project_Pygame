import random
import Database 
import Range_word_a_z
# from Data_base import Database
# from Data_base import Range_word_a_z
#choose_letter_index = random.randint(1, 26)  
#choose_word = random.randint(0, 4158)        


def word_label():
    word_instance = Database.Word()
    A_TO_Z = word_instance.change_number_to_word()
    
    dir_for_word = {}
    for i in range(len(A_TO_Z)):
        dir_for_word[i + 1] = A_TO_Z[i]  # {1: 'a', 2: 'b', ..., 26: 'z'}
        
    return dir_for_word



def generate_question(word_for_random, Data_all):
    while True:
        choose_letter_index = random.randint(1, 26)

        if choose_letter_index in word_for_random:
            letter = word_for_random[choose_letter_index]  # e.g., 'c'
            start, end = Range_word_a_z.get_range(letter)
            
            choose_word = random.randint(start, end - 1)
            
            if letter in Data_all:
                words_for_letter = Data_all[letter] 
    
                if choose_word in words_for_letter:
                    question = words_for_letter[choose_word][0]
                    answer = words_for_letter[choose_word][1]
                    return question, answer
                else:
                    continue  
            else:
                continue
        else:
            continue


class Call_Qusetion_Answer():
    def __init__(self, Data_all, word_for_ramdom):
        self.Data_all = Data_all
        self.word_for_ramdom = word_for_ramdom
    
    def Call_Q_A(self): 
       question, answer = generate_question(self.word_for_ramdom, self.Data_all)
       return question, answer                    #f'Question = {question}'

    #def Call_Answer(self):
       #question, answer = generate_question(self.word_for_ramdom, self.Data_all)
       #return  answer                     #f'Answer = {answer}'
   
   
def Qusetion_Answer():
    word_for_random = word_label()
    Data_all = Database.sent()
    Q_A = Call_Qusetion_Answer(Data_all, word_for_random)
    return Q_A.Call_Q_A()

   
#def Answer():
    #word_for_random = word_label()
    #Data_all = Database.sent()
    #Q_A = Call_Qusetion_Answer(Data_all, word_for_random)
    #return Q_A.Call_Answer()

    
