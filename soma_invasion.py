import sys
import pygame

from settings import Settings


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

    def run(self):
        while active:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.screen_color)


if __name__ == '__main__':
    soma_game = SomaGame()
    soma_game.run()            
            

            
        
        
