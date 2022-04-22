import pygame as pg
import random
pg.init()

WIN_WIDTH, WIN_HEIGHT = 1000, 800
window = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#images
IMG_BACKGROUND = pg.image.load('Images/background.png')
IMG_BIRD = pg.image.load('Images/fatBird.png')
IMG_TOP_PIPE = pg.image.load('Images/full pipe top.png')
IMG_BOTTOM_PIPE = pg.image.load('Images/full pipe bottom.png')

IMG_BACKGROUND.convert()
IMG_BIRD.convert()
IMG_TOP_PIPE.convert()
IMG_BOTTOM_PIPE.convert()

#Time stuff
clock = pg.time.Clock()
FPS = 60

#Bird stuff (Bird b)
b_x, b_y = 200, WIN_HEIGHT/2
acceleration_down = 0

#Pipe stuff
acceleration_left = 1
lst_upper_pipes = [[700, random.randint(-550, -400)], [1050, random.randint(-550, -400)], [1400, random.randint(-550, -400)]]
lst_lower_pipes = [[700, WIN_HEIGHT-random.randint(100, 300)], [1050, WIN_HEIGHT-random.randint(100, 300)], [1400, WIN_HEIGHT-random.randint(100, 300) ]]

def isectRectCircle(rect_tl, rect_size, circle_cpt, circle_rad):
    rect = pg.Rect(*rect_tl, *rect_size)
    if rect.collidepoint(*circle_cpt):
        return True

    centerPt = pg.math.Vector2(*circle_cpt)
    cornerPts = [rect.bottomleft, rect.bottomright, rect.topleft, rect.topright]
    if [p for p in cornerPts if pg.math.Vector2(*p).distance_to(centerPt) <= circle_rad]:
        return True

    return False


running = True
while running:
    #draw background
    window.blit(IMG_BACKGROUND, (0, 0))
    window.blit(IMG_BACKGROUND, (600, 0))
    #bird gravitation
    acceleration_down += 0.3
    b_y += acceleration_down
    window.blit(IMG_BIRD, (b_x-29, b_y-20))#redraw bird
    #pipe stuff
    for p in range(3):
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
        #check if bird crashed with pipe
        if (isectRectCircle(rect_tl=(lst_upper_pipes[p][0], lst_upper_pipes[p][1]), rect_size=(104, 800), circle_cpt=(b_x, b_y), circle_rad=25) == True) \
         or (isectRectCircle(rect_tl=(lst_lower_pipes[p][0], lst_lower_pipes[p][1]), rect_size=(104, 800), circle_cpt=(b_x, b_y), circle_rad=25) == True):
            running = False

        acceleration_left+=0.0001
        #pg.draw.circle(window, (255, 0, 0), (b_x, b_y), 25, 3)
    for event in pg.event.get():
        if event.type == pg.QUIT:#Exitcondition
            running = False
        if event.type == pg.KEYDOWN:#Keyboard Event(space)-> flap
            if event.key == pg.K_SPACE:
                acceleration_down = -8
    if b_y >= WIN_HEIGHT: #bird touches ground -> death
        running = False

    pg.display.update()
    pg.display.flip()
    clock.tick(FPS)
pg.quit()



