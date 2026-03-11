import tkinter as tk
import pygame

from player import Player

WHITE = (255, 255, 255)
FPS = 60

class QuizGame:
    def __init__(self, q):
        self.questions = q  # the dictionary is then received and stored
        self.SCREENWIDTH = 800
        self.SCREENHEIGHT = 600

        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))
        pygame.display.set_caption('Quiz Game')
        self.running = True
        self.clock = pygame.time.Clock()

        self.initialize()
        
    def initialize(self):
        self.playerSpriteGroup = pygame.sprite.Group()
        self.player = Player(400, 300)
        self.playerSpriteGroup.add(self.player)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()

        self.player.handle_input(keys)
        self.playerSpriteGroup.update()
        

    def draw(self):
        # clear screen
        self.screen.fill(WHITE)

        self.playerSpriteGroup.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

    
# dih = {}
# g = QuizGame(dih)

# g.run()