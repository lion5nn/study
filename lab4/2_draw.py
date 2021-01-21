import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 950))

def draw_world(width, height):
    """
    Draw the world according to the given dimensions
    :param width: The display width
    :param height: The displat height
    :return:None
    """
    pass

def draw_house(x, y, width, height):
    """
    Draw the house according to the given dimensions
    :param x: X coordinate of the upper right corner
    :param y: Y coordinate of the upper right corner
    :param width: Largest width of the house
    :param height: Largest height of the house
    :return: None
    """
    pass

def draw_ghost(x, y, width, height):
    """
    Draw the ghost according to the given dimensions
    :param x: X coordinate of the upper right corner
    :param y: Y coordinate of the upper right corner
    :param width: Largest width of the ghost
    :param height: Largest height of the ghost
    :return: None
    """
    pass

rect(screen, (59, 59, 94), (0, 0, 700, 450))
rect(screen, (0, 26, 0), (0, 450, 700, 950))
rect(screen, (51, 26, 0), (50, 200, 350, 600))
circle(screen, (250, 250, 250), (600, 100), 70)
polygon(screen, (16, 16, 16), [(75, 175), (375, 175),
                               (440, 225), (10, 225)])
rect(screen, (38, 38, 38), (150, 175, 35, -85))

d = 35
for _ in range(4):
    rect(screen, (153, 102, 0), (50+d, 225, 50, 150))
    d += 75

ellipse(screen, (41, 41, 51), (300, 100, 400, 70))
ellipse(screen, (40, 15, 0), (50, 10, 300, 60))

d = 20
for i in range(3):
    if i == 2:
        rect(screen, (230, 230, 0), (50 + d, 650, 70, 80))
        d += 120
    else:
        rect(screen, (77, 0, 0), (50+d, 650, 70, 80))
        d += 120

rect(screen, (26, 0, 0), (10, 400, 430, 60))

d = 0
for i in range(6):
    rect(screen, (26, 0, 0), (25+d, 300, 60, 100), 15)
    d += 68

circle(screen, (217, 217, 217), (550, 700), 40)
polygon(screen, (217, 217, 217), [(580, 675), (650, 880), (450, 880), (520, 675)])

d = 0
for i in range(10):
    circle(screen, (217, 217, 217), (460+d, 880), 10)
    d += 20

d = 0
for i in range(2):
    circle(screen, (102, 217, 255), (535+d, 690), 10)
    ellipse(screen, (255, 255, 255), (532+d, 684, 10, 5))
    circle(screen, (0, 0, 0), (532+d, 689), 4)
    d += 30

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
