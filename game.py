import tkinter as tk
import pygame

from player import Player
from enemy import Enemy
from bullet import Bullet

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
        
        self.enemiesSpriteGroup = pygame.sprite.Group()
        self.init_enemies()
    
    def init_enemies(self):
        amtOfEnemies = 4

        # Spread enemies evenly around the screen center
        spacing = 150
        center_x = self.SCREENWIDTH // 2
        start_x = center_x - (amtOfEnemies - 1) * spacing // 2
        y = self.SCREENHEIGHT // 2 - 100  # spawn near vertical center

        for i in range(amtOfEnemies):
            x = start_x + i * spacing
            enemy = Enemy(i,x, y)
            self.enemiesSpriteGroup.add(enemy)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()

        self.player.handle_input(keys)
        self.playerSpriteGroup.update()

        #hits = pygame.sprite.spritecollide(self.player)
        

    def draw(self):
        # clear screen
        self.screen.fill(WHITE)

        self.playerSpriteGroup.draw(self.screen)
        self.enemiesSpriteGroup.draw(self.screen)

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