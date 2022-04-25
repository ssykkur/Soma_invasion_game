import sys
import pygame

from settings import Settings
from ship import SomaShip
from pew_pew import Pew

active = True
fps = 60


class SomaGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                                self.settings.screen_height))
        pygame.display.set_caption("Soma Invasioon")
        self.clock = pygame.time.Clock()
        self.pew_pews = pygame.sprite.Group()
        self.soma_ship = SomaShip(self)

    def run(self):
        while active:
            self.clock.tick(fps)
            self._check_events()
            self.soma_ship.move_ship()
            self._update_pews()
            self._update_screen()
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.soma_ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.soma_ship.moving_left = True
        if event.key == pygame.K_SPACE:
            self._create_pew()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.soma_ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.soma_ship.moving_left = False

    def _create_pew(self):
        if len(self.pew_pews) < self.settings.max_pew:
            new_pew = Pew(self)
            self.pew_pews.add(new_pew)

    def _update_pews(self):
        self.pew_pews.update()
        for pew in self.pew_pews.copy():
            if pew.rect.bottom <= 0:
                self.pew_pews.remove(pew)


    def _update_screen(self):
        self.screen.fill(self.settings.screen_color)
        self.soma_ship.blit_ship()
        for pew in self.pew_pews:
            pew.draw_pew()
        pygame.display.flip()


if __name__ == '__main__':
    soma_game = SomaGame()
    soma_game.run()            
            

            
        
        
