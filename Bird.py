import pygame as pg
class FlappyBird:
    def __init__(self, y):
        self.x_pos = 80
        self.y_pos = y
        self.dead = False
        self.img_bird = pg.image.load("Images/fatBird.png")
        self.hitbox = (self.x_pos, self.y_pos, self.img_bird.get_width(), self.img_bird.get_height())
    def draw_Bird(self, screen):
        screen.blit(self.img_bird, (self.x_pos,self.y_pos))

    def set_y_pos(self, y):
        self.y_pos = y
    def get_y_pos(self):
        return self.y_pos
