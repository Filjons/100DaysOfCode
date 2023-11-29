# the quiz brain will run the quiz and keep track of the questions and answers.

class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
    
    def next_question(self):
        q = None
        if self.question_number < len(self.question_list)-2:
            self.question_number += 1
            n = self.question_number
            q = self.question_list[n]
            
        return q
        
    