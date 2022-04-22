import pygame as pg
from Bird import FlappyBird
from pipe import pipe
pg.init()

class gameWindow:
  def __init__(self, window_title='Flappy Bird'):
    #setup attributes
    self.background_image = pg.image.load("Images/background.png")
    self.background_colour = (255,255,255)
    self.width = self.background_image.get_width()
    self.height = self.background_image.get_height()
    self.clock = pg.time.Clock()
    self.init_objects()
    self.acceleration = 0

    #setup gamewindow stuff

    pg.display.set_caption(window_title)
    self.screen = pg.display.set_mode((self.width, self.height))
    self.screen.fill(self.background_colour)
    pg.display.flip()
    self.set_running()

  def game_loop(self):
    self.acceleration = 0.01

    while self.running:
      self.screen.blit(self.background_image, (0, 0))
      self.acceleration += 0.01

      ###

      self.bird.set_y_pos(self.bird.get_y_pos() + self.acceleration)
      for p in self.pipes:
        p.set_x_pos(p.get_x_pos()-0.15) #move the pipes to the left
      ###
      for event in pg.event.get():
        if event.type == pg.QUIT:
          self.unset_running()
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_SPACE:
            self.acceleration = -1.6
      self.redraw_window()
      self.clock.tick(300)

  def init_objects(self):
    self.bird = FlappyBird(0.5 * self.height - 20)

    #init pipes
    self.pipes = [
      pipe(int(self.background_image.get_width() * 0.6), -500, True),
      pipe(int(self.background_image.get_width()*1.0), -400, True),
      pipe(int(self.background_image.get_width() * 1.4), -450, True),
      pipe(int(self.background_image.get_width() * 1.8), -700, True),

      pipe(int(self.background_image.get_width() * 0.6), 600, False),
      pipe(int(self.background_image.get_width() * 1.0), 700, False),
      pipe(int(self.background_image.get_width() * 1.4), 600, False),
      pipe(int(self.background_image.get_width() * 1.8), 350, False)
    ]
  def redraw_window(self):
    #self.screen.blit(self.background_image, (0, 0))
    self.bird.draw_Bird(self.screen)

    for p in self.pipes:
      p.draw_pipe(self.screen)
    pg.display.update()

  def set_running(self):
    self.running = True
  def unset_running(self):
    self.running = False
