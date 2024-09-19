from tkinter import *
from quiz_brain import QuizBrain
MID = "#B0C5A4"
LIGHT = "#ECE3CE"
DARK = "#739072"
RED = "#D37676"


class Interface:
    """Handles all the GUI creation"""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window and Canvas Config
        self.window = Tk()
        self.window.config(height=200, width=100, bg=DARK, pady=25, padx=25)
        self.window.minsize(250, 150)
        self.canvas = Canvas(width=450, height=250, bg=LIGHT, highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=3, padx=20, pady=20)

        # Labels
        self.user_score = Label(text=f"Score:{self.quiz.score}/{self.quiz.question_number}", bg=DARK, fg=LIGHT,
                                font=("futura", 20, "bold"))
        self.user_score.grid(column=0, row=0, columnspan=3)
        self.text = Label(text="Welcome to True or False! There are 10 questions total.\nGood luck!",
                          fg=DARK, bg=LIGHT, font=("futura", 20, "bold"))
        self.text.config(wraplength=300)
        self.text.grid(column=1, row=1)

        # Buttons
        self.true = Button(command=self.check_answer_true, text="True", highlightthickness=0, bg=MID, fg="white",
                           font=("futura", 20, "bold"))
        self.true.grid(column=0, row=3)
        self.false = Button(command=self.check_answer_false, text="False", highlightthickness=0, bg=RED, fg="white",
                            font=("futura", 20, "bold"))
        self.false.grid(column=2, row=3)

        self.window.after(5000, self.get_next_question)
        self.window.mainloop()

    def get_next_question(self):
        """Handles changing of questions"""
        if self.quiz.question_number < 10:
            q_text = self.quiz.next_question()
            self.text.config(text=q_text, font=("futura", 16, "bold"))
        else:
            self.text.config(text=f"Finished!\n You scored {self.quiz.score}/10")
            self.true.destroy()
            self.false.destroy()
            self.window.after(8000, self.window.destroy)

    def check_answer_false(self):
        """On button click, checks if the answer is false and updates the score accordingly."""
        self.quiz.check_answer("False")
        self.user_score.config(text=f"Score:{self.quiz.score}/{self.quiz.question_number}")
        self.get_next_question()

    def check_answer_true(self):
        """On button click, checks if the answer is true and updates the score accordingly."""
        self.quiz.check_answer("True")
        self.user_score.config(text=f"Score:{self.quiz.score}/{self.quiz.question_number}")
        self.get_next_question()
