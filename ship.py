import pygame 
from pygame.sprite import Sprite


class SomaShip(Sprite):
    def __init__(self, soma_game_instance):
        super().__init__()
        self.screen = soma_game_instance.screen
        self.settings = soma_game_instance.settings
        self.screen_rect = self.screen.get_rect()
        self.image = self.settings.scale_img(pygame.image.load('assets/soma_ship.png'), 2.5)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def move_ship(self):
        if self.moving_right and self.rect.right < self.settings.screen_width:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x


    def blit_ship(self):
        self.screen.blit(self.image, self.rect)

    