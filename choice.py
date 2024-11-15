import random
import Database 
import A_TO_Z_range
import pull


    
#Q1_in_box = Choice()
#Qusetion1 = sent_pull.Qusetion()
#print(Qusetion1)
class build_Qusetion:    # pull data form data datadase
    def __init__(self, Need_total_Qusetion, choice):
        self.Need_total_Qusetion = Need_total_Qusetion
        self.choice = choice
        
    def total_Qusetion(self):
        keep_all_qusetion = [pull.Qusetion_Answer() for i in range(self.Need_total_Qusetion)]
        return keep_all_qusetion
    
    def total_choice(self):
        keep_all_choice = [pull.Qusetion_Answer()[0] for i in range(self.choice)]
        return keep_all_choice

class clean_Qustion(build_Qusetion):
    
    def __init__(self, Need_total_Qusetion, choice):
        super().__init__(Need_total_Qusetion, choice)
      
    def clean_qustion(self): # if qusetion form random duplicate
    
        while True:
            q = build_Qusetion(self.Need_total_Qusetion, self.choice)
            Q = q.total_Qusetion()
            number_qusetion = len(Q)
            for i in range(number_qusetion - 1):
                if Q[i][0] != Q[i + 1][0]:
                   return Q
                else:
                    continue
    def clean_answer(self): # if Answer form random duplicate in list 
    #q = build_Qusetion(Need_total_Qusetion=5, choice=15)
        while True:
            a = build_Qusetion(self.Need_total_Qusetion, self.choice)
            A = a.total_choice()
            number_answer = len(A)
            for i in range(number_answer - 1):
                if A[i] != A[i + 1]:
                   return A
                else:
                    continue

    
class qusetion_eqution_answer(build_Qusetion):  # if qusetion eqution answer form random
    
    def __init__(self, Need_total_Qusetion, choice):
        super().__init__(Need_total_Qusetion, choice)
    
    def check_qusetion(self):
        while True:
            Q = clean_Qustion(self.Need_total_Qusetion, self.choice)
            Q_check = Q.clean_qustion()
            A_check = Q.clean_answer()
            Q_check_len = len(Q_check)
            for i in range(Q_check_len):
                if  Q_check[i][0] not in A_check:
                    return Q_check, A_check
                else:
                    continue          
        
Q_A_check = qusetion_eqution_answer(Need_total_Qusetion=5, choice=15)
check_Q, check_A = Q_A_check.check_qusetion()

print(check_Q) # ['word', 'tran']
print(check_A) # ['word', 'word', 'word' 'word']  