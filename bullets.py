import pygame
from os.path import join

class Bullet(pygame.sprite.Sprite):
    def __init__(self,init_x,init_y):
        super().__init__()

        # Draw bullets in a contrasting color so they are visible over the white background
        self.image = pygame.Surface((4,10), pygame.SRCALPHA)
        self.image.fill((255, 50, 50))  # red
        
        self.pos_x = init_x
        self.pos_y = init_y

        self.rect = self.image.get_frect(center=(self.pos_x,self.pos_y))

        self.speed = 5
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0 or self.rect.top > 600:
            self.kill()

    def handle_input(self):
        pass
#ww
class PlayerBullet(Bullet):
    def __init__(self, x, y):
        super().__init__(x, y)  
        self.speed = -8 # moves upward

    def update(self):
        super().update()


class EnemyBullet(Bullet):
    def __init__(self, x, y):
        super().__init__(x, y)  
        self.speed = 5 # moves downward

    def update(self):
        super().update()