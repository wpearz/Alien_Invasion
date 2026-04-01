import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self,blck):
        super().__init__()
        self.screen = blck.screen
        self.settings = blck.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at(0,0)and then set correct position.
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = blck.ship.rect.midtop

        #store the bullet's position as a float.
        self.y = float(self.rect.y)
        
    def update(self):
        """Move the bullet up the screen."""
        #update the exact porition of the bullet.
        self.y -= self.settings.bullet_speed

        #update the rect poisition
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color, self.rect)


    
