from pygame.sprite import Sprite

class Pew(Sprite):
    def __init__(self, soma_game_instance):
        super().__init__()
        self.screen = soma_game_instance.screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.settings.pew_pew_width, 
                                pew_pew_height)
        self.rect.midtop = self.soma_ship.midtop
        self.y = float(self.rect.y)

    def shoot(self):
        self.y -= self.settings.pew_pew_speed
        self.rect.y = self.y