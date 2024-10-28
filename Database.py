# I will keep data form class with type data is dir

class Vocabculary:
    def __init__(self, vocab_type, vocab):
        self.vocab_type = vocab_type
        self.vocab = vocab
        
        
    def show_data(self):
        print(f'vocab_all {self.vocab_type}')
        print(f'vocab {self.vocab}')
        
    
    def keep_data(self):
        vocab = self.vocab


class Daily_Rotine(Vocabculary):
    rotine = {'brush my teeth' : 'แปรงฟัน', 
              'Eat dinner' : 'กินอาหารเย็น'}
    def __init__(self, vocab_type, vocab):
        super().__init__(vocab_type, self.rotine)
        

vocab = Daily_Rotine('vocab' , '2')
vocab.show_data()

    
        