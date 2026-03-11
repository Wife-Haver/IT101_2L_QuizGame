import pygame
from os.path import join

PLAYER_SPEED = 7



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        
        self.image = pygame.image.load(join('assets','ship.png')).convert_alpha()
        self.image = transformScaleKeepRatio(self.image,(50,50))
        
        
        # get the rectangle for positioning
        self.rect = self.image.get_frect()
        self.rect.x = x # starting x pos
        self.rect.y = y # starting y pos
        
        # movement variables
        self.speed = PLAYER_SPEED
        self.direction = pygame.math.Vector2(0, 0)
    
    def update(self):
        # update player position based on direction
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        
        # keep player on screen
        self.rect.clamp_ip(pygame.display.get_surface().get_rect())
    
    def handle_input(self, keys):
        # reset direction
        self.direction.x = 0
        self.direction.y = 0
        
        # set direction using key presses
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1

        if keys[pygame.K_SPACE]:
            #s TODO hoot 
            pass
        
        # normalize diagonal movement forconsistent speed
        if self.direction.length() > 0:
            self.direction.normalize_ip()
        
        # def shoot():
        #     bullet = 



def transformScaleKeepRatio(image, size):
    #Scales 'image' to fit into 'size' box while keeping aspect ratio.
    iwidth, iheight = image.get_size()
    scale = min(size[0] / iwidth, size[1] / iheight)
    new_size = (round(iwidth * scale), round(iheight * scale))
    scaled_image = pygame.transform.scale(image, new_size)
    #image_rect = scaled_image.get_frect(center=(size[0] // 2, size[1] // 2))
    return scaled_image