import tkinter as tk 
from PIL import Image, ImageTk



class QuizGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x600')

        self.canvas = tk.Canvas(self.root, width=500, height=500, bg='white')
        self.canvas.pack()

        self.spaceshipImg = Image.open('assets/ship.png')
        self.spaceshipImg = self.spaceshipImg.resize((40,40))
        self.spaceshipSprite = ImageTk.PhotoImage(self.spaceshipImg)

        self.spaceship = self.canvas.create_image(250,250,image=self.spaceshipSprite,tags = 'player')

        #movement speed
        self.speed = 10


        # Track pressed keys
        self.keys_pressed = set()

        self.root.bind('<KeyPress>', self.key_press)
        self.root.bind('<KeyRelease>', self.key_release)
        
        self.move_loop()
        
        # Ensure canvas gets focus for key events
        self.canvas.focus_set()
        
    def key_press(self, event):
        self.keys_pressed.add(event.keysym.lower())
        
    def key_release(self, event):
        self.keys_pressed.discard(event.keysym.lower())

    def move_loop(self):
        dx = 0
        dy = 0
        
        if 'w' in self.keys_pressed:
            dy = -self.speed
        if 's' in self.keys_pressed:
            dy = self.speed
        if 'a' in self.keys_pressed:
            dx = -self.speed
        if 'd' in self.keys_pressed:
            dx = self.speed
            
        if dx != 0 or dy != 0:
            self.canvas.move('player', dx, dy)
            
        self.root.after(20, self.move_loop)

game = QuizGame()

game.root.mainloop()