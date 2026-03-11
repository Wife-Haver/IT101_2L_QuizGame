import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self,initial_pos:tuple):
        self.pos_x,self.pos_y = initial_pos
    
    def update(self):
        pass

    def handle_input(self):
        pass

