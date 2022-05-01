import pygame as pg
import random
pg.init()

WIN_WIDTH, WIN_HEIGHT = 1000, 800
window = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# images
IMG_BACKGROUND = pg.image.load('Images/background.png')
IMG_TOP_PIPE = pg.image.load('Images/full pipe top.png')
IMG_BOTTOM_PIPE = pg.image.load('Images/full pipe bottom.png')
IMG_GROUND = pg.image.load('Images/groundPiece.png')

IMG_BACKGROUND.convert()
IMG_GROUND.convert()
IMG_TOP_PIPE.convert()
IMG_BOTTOM_PIPE.convert()

# Time stuff
clock = pg.time.Clock()
FPS = 60


# Bird stuff (Bird b)
class Bird:
    IMG_BIRD = pg.image.load('Images/fatBird.png')
    x, y = 200, WIN_HEIGHT / 2
    acceleration_down = 0

    def __init__(self):
        self.IMG_BIRD.convert()

    def is_bird_colliding(self, idx_pipe):
        # check y
        if (self.y-(self.IMG_BIRD.get_height()/2) < lst_upper_pipes[idx_pipe][1]+IMG_TOP_PIPE.get_height()) \
         or (self.y+(self.IMG_BIRD.get_height()/2) > lst_lower_pipes[idx_pipe][1]):
            # check x
            if ((self.x + (self.IMG_BIRD.get_width()/2) >= lst_upper_pipes[idx_pipe][0]) \
             and (self.x + (self.IMG_BIRD.get_width()/2) <= lst_upper_pipes[idx_pipe][0]+IMG_TOP_PIPE.get_width())) \
             or ((self.x - (self.IMG_BIRD.get_width()/2) <= lst_upper_pipes[idx_pipe][0]+IMG_TOP_PIPE.get_width())
             and (self.x - (self.IMG_BIRD.get_width()/2) >= lst_upper_pipes[idx_pipe][0])):
                    return True

        if self.y+(self.IMG_BIRD.get_height()/2) >= WIN_HEIGHT-IMG_GROUND.get_height(): #aufprall am Boden
            return True
        if self.y-(self.IMG_BIRD.get_height()/2) <= 0: #tod durch Sauerstoff mangel
            return True


def draw_everything():
    window.blit(IMG_BACKGROUND, (0, 0))
    window.blit(IMG_BACKGROUND, (600, 0))
    for b in lst_birds:
        window.blit(b.IMG_BIRD, (b.x - b.IMG_BIRD.get_width() / 2, b.y - b.IMG_BIRD.get_height() / 2))
    for p in range(len(lst_upper_pipes)):
        window.blit(IMG_TOP_PIPE, (lst_upper_pipes[p][0], lst_upper_pipes[p][1]))
        window.blit(IMG_BOTTOM_PIPE, (lst_lower_pipes[p][0], lst_lower_pipes[p][1]))
    # draw ground
    number_of_goundpieces = int(WIN_WIDTH / IMG_GROUND.get_width()) + 1
    for i in range(number_of_goundpieces):
        window.blit(IMG_GROUND, (i * IMG_GROUND.get_width(), WIN_HEIGHT - IMG_GROUND.get_height()))
    pg.display.update()
    pg.display.flip()

lst_upper_pipes = []
lst_lower_pipes = []
lst_birds = []

counter_attempts = 0
game = True
while game:
    counter_attempts += 1
    #add bird
    lst_birds.clear()
    lst_birds.append(Bird())

    # add pipes
    lst_upper_pipes.clear()
    lst_upper_pipes.append([700, random.randint(-550, -400)])
    lst_upper_pipes.append([1050, random.randint(-550, -400)])
    lst_upper_pipes.append([1400, random.randint(-550, -400)])

    lst_lower_pipes.clear()
    lst_lower_pipes.append([700, WIN_HEIGHT-random.randint(100, 300)])
    lst_lower_pipes.append([1050, WIN_HEIGHT-random.randint(100, 300)])
    lst_lower_pipes.append([1400, WIN_HEIGHT-random.randint(100, 300) ])
    #move pipe left **modify if pipe should move faster
    acceleration_left = 1.2

    draw_everything()# first drawing

    # wating for user interaction

    running = True
    while running:
        #draw background
        window.blit(IMG_BACKGROUND, (0, 0))
        window.blit(IMG_BACKGROUND, (600, 0))
        #bird gravitation

        for b in lst_birds:
            b.acceleration_down += 0.3
            b.y += b.acceleration_down
            window.blit(b.IMG_BIRD, (b.x-b.IMG_BIRD.get_width()/2, b.y-b.IMG_BIRD.get_height()/2))#redraw bird

        #pipe stuff
        for p in range(len(lst_upper_pipes)):
            lst_upper_pipes[p][0] -= acceleration_left
            lst_lower_pipes[p][0] -= acceleration_left
            window.blit(IMG_TOP_PIPE, (lst_upper_pipes[p][0], lst_upper_pipes[p][1]))
            window.blit(IMG_BOTTOM_PIPE, (lst_lower_pipes[p][0], lst_lower_pipes[p][1]))

            #pipes go to the other side again
            if lst_upper_pipes[p][0] < 0:
                lst_upper_pipes[p][0] = WIN_WIDTH
                lst_lower_pipes[p][0] = WIN_WIDTH
                lst_upper_pipes[p][1] = random.randint(-550, -400)
                lst_lower_pipes[p][1] = WIN_HEIGHT-random.randint(100, 300)
            # check if bird crashed with pipe
            for b in lst_birds:
                if b.is_bird_colliding(p):
                    del b
                    running = False

            acceleration_left += 0.0001
            # pg.draw.circle(window, (255, 0, 0), (b_x, b_y), 25, 3)

        # draw ground
        number_of_goundpieces = int(WIN_WIDTH/IMG_GROUND.get_width()) + 1
        for i in range(number_of_goundpieces):
            window.blit(IMG_GROUND, (i * IMG_GROUND.get_width(), WIN_HEIGHT-IMG_GROUND.get_height()))

        # event stuff
        for event in pg.event.get():
            if event.type == pg.QUIT:# Exitcondition
                running = False
                game = False
            if event.type == pg.KEYDOWN:#Keyboard Event(space)-> flap
                if event.key == pg.K_SPACE:
                    for b in lst_birds:
                        b.acceleration_down = -8
                if event.key == pg.K_ESCAPE:
                    running = False
                    game = False

        pg.display.update()
        pg.display.flip()
        clock.tick(FPS)
pg.quit()
