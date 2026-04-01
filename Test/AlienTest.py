import sys
import pygame

pygame.init()

from settings import Settings
from ship import Ship

class AlienTwo:

    def __init__(self):
         pygame.init()
         self.settings = Settings()
         self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
         self.clock = pygame.time.Clock()
         self.ship = Ship(self)
         pygame.display.set_caption("Alien2")

###############
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
        self.clock.tick(60)
#
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:

                self._check_keyup_events(event)
    


    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            self.ship.moving_left = False
        
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            self.ship.moving_right = False
        if event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
    
    def _check_keyup_events(self,event):

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
         
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()



if __name__ == '__main__':
    bck = AlienTwo()
    bck.run_game()
  
