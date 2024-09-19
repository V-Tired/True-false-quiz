from tkinter import *

# Colors
MID = "#B0C5A4"
LIGHT = "#ECE3CE"
DARK = "#739072"
RED = "#D37676"


class QuizBrain:
    """A class to handle the questions, requires question list"""
    def __init__(self, q_list: list):
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None
        self.score = 0

    def next_question(self) -> str:
        """Cycles through the 10 questions, returns the count"""
        if self.question_number < 10:
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            return f"Q.{self.question_number}\n{self.current_question.text}"

    def check_answer(self, user_answer: str):
        """Compares user response to the correct answer and updates the user score accordingly."""
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1

