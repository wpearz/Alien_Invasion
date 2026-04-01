import pygame


class Ship:
    """A class to manage the ship."""
    def __init__(self,w):
        """Initialize the ship and set its starting position."""
        self.screen = w.screen
        self.screen_rect = w.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load(r"C:\Users\a\Documents\python_projects\AlienInvision\images\ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self):
        # speed of the ship
        speed = 20

        
        if self.rect.right < self.screen_rect.right:
            if self.moving_right:
                self.rect.x += speed

        if self.rect.left > 0 :
            if self.moving_left:
                self.rect.x -= speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
