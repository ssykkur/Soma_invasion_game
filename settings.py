import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = 89, 55, 100
        self.ship_speed = 5
        self.pew_pew_width = 5
        self.pew_pew_height = 10
        self.pew_pew_speed = 8
        self.pew_pew_color = 48, 96, 130
        self.max_pew = 3

    def scale_img(self, img, factor):
        size = round(img.get_width() * factor), round(img.get_height() * factor)
        return pygame.transform.scale(img, size)