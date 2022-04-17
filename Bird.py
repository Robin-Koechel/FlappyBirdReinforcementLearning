import pygame as pg
class FlappyBird:
    def __init__(self, y):
        self.x_pos = 80
        self.y_pos = y
        self.dead = False
        self.img_bird = pg.image.load("Images/fatBird.png")

    def draw_Bird(self, screen):
        screen.blit(self.img_bird, (self.x_pos,self.y_pos))

    def set_y_pos(self, y):
        self.y_pos = y
    def get_y_pos(self):
        return self.y_pos
    def get_mass(self):
        return self.mass