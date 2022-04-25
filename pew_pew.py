from pygame.sprite import Sprite
import pygame

class Pew(Sprite):
    def __init__(self, soma_game_instance):
        super().__init__()
        self.screen = soma_game_instance.screen

        self.settings = soma_game_instance.settings
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.settings.pew_pew_width, 
                                self.settings.pew_pew_height)
        self.rect.midtop = soma_game_instance.soma_ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.pew_pew_speed
        self.rect.y = self.y

    def draw_pew(self):
        pygame.draw.rect(self.screen, self.settings.pew_pew_color, self.rect)