from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

'''
TODO
* asking the question
* checking if the answer was correct
* checking if we're at the end of the quiz
'''

# convert question data into Question objects and save them to a list for easier access.
question_bank = []
for data in question_data:
    text = data['text']
    answer = data['answer']
    new_question = Question(q_text=text, q_answer=answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

# Start the game

while quiz_brain.has_question():

    print(f"Score: {quiz_brain.get_score()}")

    question = quiz_brain.next_question()

    # ask the user the question and take an answer
    player = input(f"Question {quiz_brain.question_number}: {question.text} (True/False)?: ").capitalize()

    # check the answer and add score
    if quiz_brain.check_answer(player,question.answer):
        quiz_brain.add_score()

print(f"That's it! You got {quiz_brain.get_score()} / {quiz_brain.question_number} answers right!")