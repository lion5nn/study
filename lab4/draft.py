import pygame
from pygame.draw import *
from math import ceil

screen = pygame.display.set_mode((700, 950))


def main():
    """
    It is the main game cycle
    :return: None
    """
    pygame.init()
    fps = 30
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True


def draw_environment(width, height):
    """
    Draw environment
    :param width: Full screen width
    :param height: Full screen height
    :return: None
    """
    sky_width = width
    sky_height = ceil(0.5 * height)
    draw_sky((59, 59, 94), sky_width, sky_height)

    moon_x = ceil(0.9 * width)
    moon_y = ceil(0.1 * height)
    moon_size = ceil(0.1 * width)
    draw_moon((250, 250, 250), moon_x, moon_y, moon_size)

    first_cloud_x = ceil(0.4 * width)
    first_cloud_y = ceil(0.1 * height)
    first_cloud_width = ceil(0.6 * height)
    first_cloud_height = ceil(0.07 * height)
    draw_cloud((41, 41, 51), first_cloud_x, first_cloud_y,
               first_cloud_width, first_cloud_height)

    second_cloud_x = ceil(0.1 * width)
    second_cloud_y = ceil(0.01 * height)
    second_cloud_width = ceil(0.4 * height)
    second_cloud_height = ceil(0.06 * height)
    draw_cloud((40, 15, 0), second_cloud_x, second_cloud_y,
               second_cloud_width, second_cloud_height)


def draw_sky(color, sky_width, sky_height):
    """
    Draw the sky
    :param color: Sky color
    :param sky_width: Max sky width
    :param sky_height: Max sky height
    :return: None
    """
    rect(screen, color, (0, 0, sky_width, sky_height))


def draw_moon(color, moon_x, moon_y, moon_size):
    """
    Draw the Moon
    :param color: Moon color
    :param moon_x: X coordinate of the Moon
    :param moon_y: Y coordinate of the Moon
    :param moon_size: Moon radius
    :return: None
    """
    circle(screen, color, (moon_x, moon_y), moon_size)


def draw_cloud(color, x, y, width, height):
    """
    Draw a cloud
    :param color: Cloud color
    :param x: X coordinate of the cloud
    :param y: Y coordinate og the cloud
    :param width: Max cloud width
    :param height: Max cloud height
    :return: None
    """
    ellipse(screen, color, (x, y, width, height))


def draw_house(x, y, width, height):
    """
    Draw house
    :param x: X coordinate upper left point of house
    :param y: Y coordinate upper left point of house
    :param width: Max house width
    :param height: Max house height
    :return: None
    """
    rect(screen, (51, 26, 0), (50, 200, 350, 600))
    polygon(screen, (16, 16, 16), [(75, 175), (375, 175),
                                   (440, 225), (10, 225)])
    rect(screen, (38, 38, 38), (150, 175, 35, -85))
    d = 35
    for _ in range(4):
        rect(screen, (153, 102, 0), (50 + d, 225, 50, 150))
        d += 75

    d = 20
    for i in range(3):
        if i == 2:
            rect(screen, (230, 230, 0), (50 + d, 650, 70, 80))
            d += 120
        else:
            rect(screen, (77, 0, 0), (50 + d, 650, 70, 80))
            d += 120

    rect(screen, (26, 0, 0), (10, 400, 430, 60))

    d = 0
    for i in range(6):
        rect(screen, (26, 0, 0), (25 + d, 300, 60, 100), 15)
        d += 68


def draw_ghost(x, y, width, height):
    """
    Draw ghost
    :param x: X coordinate lower left point of ghost
    :param y: Y coordinate upper left point of ghost
    :param width: Max ghost width
    :param height: Max ghost height
    :return: None
    """
    circle(screen, (217, 217, 217), (550, 700), 40)
    polygon(screen, (217, 217, 217), [(580, 675), (650, 880), (450, 880), (520, 675)])

    d = 0
    for i in range(10):
        circle(screen, (217, 217, 217), (460 + d, 880), 10)
        d += 20

    d = 0
    for i in range(2):
        circle(screen, (102, 217, 255), (535 + d, 690), 10)
        ellipse(screen, (255, 255, 255), (532 + d, 684, 10, 5))
        circle(screen, (0, 0, 0), (532 + d, 689), 4)
        d += 30


draw_environment(700, 950)
draw_house(10, 10, 1, 1)
draw_ghost(1, 1, 1, 1)
main()
