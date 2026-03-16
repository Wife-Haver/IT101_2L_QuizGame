import tkinter as tk
from tkinter import ttk
import pygame
import sys

from game import QuizGame

class MainProgram:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tite")
        self.root.geometry('800x600')

        self.place_ui()
    
    def place_ui(self):
        mainFrame = ttk.Frame(self.root,padding=10)
        mainFrame.pack(fill=tk.BOTH,expand=True)

        label = ttk.Label(mainFrame,text='Tkinter Window',padding=10)
        label.pack(pady=20)

        button = ttk.Button(mainFrame,text='RUN GAME',command=self.run_game)

        button.pack()
    
    def run_ui(self):
        self.root.mainloop()

    def run_game(self):
        self.root.destroy()
        """this variable is where the questions are stored as a dictionary and 
        is then passed into the quiz game class/instance as a parameter to be e used"""

        dict = {}
        # endregion 
        print("running game")
        game = QuizGame(dict)
        game.run()

if __name__=="__main__":
    app = MainProgram()
    app.run_ui()