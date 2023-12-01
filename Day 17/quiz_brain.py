# the quiz brain will run the quiz and keep track of the questions and answers.

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def add_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def has_question(self):

        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):

        self.question_number += 1
        n = self.question_number - 1

        return self.question_list[n]

    def check_answer(self, guess, answer):

        if guess.lower() == answer.lower():
            print("Correct!")
            return True
        else:
            print(f"Wrong! The answer is {answer}.")
            return False
