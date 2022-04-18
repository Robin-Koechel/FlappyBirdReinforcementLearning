import pygame as pg
class pipe:
    def __init__(self, pos_x, pos_y, is_top=True):
        if is_top:
            self.img_pipe = pg.image.load("Images/full pipe top.png")
        else:
            self.img_pipe = pg.image.load("Images/full pipe bottom.png")
        self.x_pos = pos_x
        self.y_pos = pos_y
        self.hitbox = (self.x_pos, self.y_pos, self.img_pipe.get_width(), self.img_pipe.get_height())

    def draw_pipe(self, screen):
        screen.blit(self.img_pipe, (self.x_pos, self.y_pos))

    def set_x_pos(self, x):
        self.x_pos = x
    def get_x_pos(self):
        return self.x_pos