import html
from quiz_brain import QuizBrain
from question_model import Question
from data import Data
from ui import Interface

"""A true-false quiz using the API from open trivia database"""

data = Data()
question_bank = []

for question in data.q_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = Interface(quiz)

