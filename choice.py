import random
import Database 
import Range_word_a_z
import sent_pull


class Choice:
    def __init__(self):
        self.keep_question = []

    def question_called(self, q1):
        self.keep_question.append(q1)
        return self.keep_question
    
    def choice(self, c1, c2, c3, c4):
        
        pass

    
Q1_in_box = Choice()
#Qusetion1 = sent_pull.Qusetion()
#print(Qusetion1)
class build_Qusetion:
    def __init__(self, Need_total_Qusetion, choice):
        self.Need_total_Qusetion = Need_total_Qusetion
        self.choice = choice
        
    def total_Qusetion(self):
        keep_all_qusetion = [sent_pull.Qusetion_Answer() for i in range(self.Need_total_Qusetion)]
        return keep_all_qusetion
    
    def total_choice(self):
        keep_all_choice = [sent_pull.Qusetion_Answer()[0] for i in range(self.choice)]
        return keep_all_choice
''' 
class create_choice(build_Qusetion):
    sent_pull.Qusetion_Answer()
    def __init__(self, Need_total_Qusetion, choice):
        super().__init__(Need_total_Qusetion, choice, self.Word)
        keep_all_choice = [self.Word for i in range(self.choice)]
        return keep_all_choice
'''     
#one_game =  build_Qusetion(6)
#print(one_game.total_Qusetion())

first_game =  build_Qusetion(Need_total_Qusetion=4, choice=3)
print(first_game.total_choice())
        
#Need_total_Qusetion = 4

#li_choice = [sent_pull.Qusetion_Answer() for i in range(4)]
#print(li_choice)

#[('yappy', 'ช่างพูด'), ('underwater', 'ซึ่งอยู่ใต้น้ำ'), ('egret', 'นกกระยางชนิดหนึ่ง'), ('Iran', 'อิหร่าน')]
#Q1 = Q1_in_box.question_called(Qusetion1)
#print(Q1)

        
        

    

# function zip