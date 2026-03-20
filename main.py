import tkinter as tk
from tkinter import ttk
import pygame
import sys

from game import QuizGame
from parsefile import parse_quiz_file


class MainProgram:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Program")
        self.root.geometry('800x600')

        # Store quiz data here
        self.quiz_data = None

        self.place_ui()
    
    def place_ui(self):
        mainFrame = ttk.Frame(self.root, padding=10)
        mainFrame.pack(fill=tk.BOTH, expand=True)

        label = ttk.Label(mainFrame, text='Tkinter Window', padding=10)
        label.pack(pady=20)

        # Load File Button
        load_button = ttk.Button(
            mainFrame,
            text='LOAD QUIZ FILE',
            command=self.load_quiz
        )
        load_button.pack(pady=10)

        # Run Game Button
        run_button = ttk.Button(
            mainFrame,
            text='RUN GAME',
            command=self.run_game
        )
        run_button.pack(pady=10)
    
    def load_quiz(self):
        """Opens file dialog and loads quiz into memory"""
        self.quiz_data = parse_quiz_file()

        if self.quiz_data:
            print("Quiz loaded successfully!")
        else:
            print("No quiz loaded.")

    def run_ui(self):
        self.root.mainloop()

    def run_game(self):
        if not self.quiz_data:
            print("No quiz loaded! Using default quiz.")
            
            # fallback quiz
            quiz = {
                "q1": {
                    "question": "What keyword is used to define a function in Python?",
                    "A": "func",
                    "B": "define",
                    "C": "def",
                    "D": "function",
                    "correct": "C"
                }
            }
        else:
            # Convert parsed format → game format
            quiz = {}

            for i, q_data in self.quiz_data.items():
                question_text = list(q_data.keys())[0]
                answers = q_data[question_text]

                quiz[f"q{i}"] = {
                    "question": question_text,
                    "A": answers.get("A"),
                    "B": answers.get("B"),
                    "C": answers.get("C"),
                    "D": answers.get("D"),
                    "correct": answers.get("Correct")
                }

        print("running game")

        #removes tkinter window
        self.root.destroy()

        game = QuizGame(quiz) # runs game
        game.run()


if __name__ == "__main__":
    app = MainProgram()
    app.run_ui()