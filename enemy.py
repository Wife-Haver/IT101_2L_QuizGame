import pygame
from os.path import join
from player import transformScaleKeepRatio


class Enemy(pygame.sprite.Sprite):
    def __init__(self,letter_index,x,y):
        super().__init__()
        self.sprites = ["invaderA.png","invaderB.png","invaderC.png","invaderD.png"]
        self.chosen_sprite = self.sprites[letter_index]

        # Friendly name for debug / logging
        self.name = f"Enemy {chr(ord('A') + letter_index)}"

        self.image = pygame.image.load(join('assets',self.chosen_sprite)).convert_alpha()
        self.image = transformScaleKeepRatio(self.image,(50,50))

        # get the rectangle for positioning/hitbox
        self.rect = self.image.get_frect()
        self.rect.x = x # starting x pos
        self.rect.y = y # starting y pos
