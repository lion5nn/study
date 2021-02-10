import pygame
from pygame.draw import *
from math import ceil

screen = pygame.display.set_mode((900, 1000))


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
    _draw_sky((59, 59, 94), sky_width, sky_height)

    moon_x = ceil(0.9 * width)
    moon_y = ceil(0.1 * height)
    moon_size = ceil(0.1 * width)
    _draw_moon((250, 250, 250), moon_x, moon_y, moon_size)

    first_cloud_x = ceil(0.4 * width)
    first_cloud_y = ceil(0.1 * height)
    first_cloud_width = ceil(0.6 * height)
    first_cloud_height = ceil(0.07 * height)
    _draw_cloud((41, 41, 51), first_cloud_x, first_cloud_y,
               first_cloud_width, first_cloud_height)

    second_cloud_x = ceil(0.1 * width)
    second_cloud_y = ceil(0.01 * height)
    second_cloud_width = ceil(0.4 * height)
    second_cloud_height = ceil(0.06 * height)
    _draw_cloud((40, 15, 0), second_cloud_x, second_cloud_y,
               second_cloud_width, second_cloud_height)


def _draw_sky(color, sky_width, sky_height):
    """
    Draw the sky
    :param color: Sky color
    :param sky_width: Max sky width
    :param sky_height: Max sky height
    :return: None
    """
    rect(screen, color, (0, 0, sky_width, sky_height))


def _draw_moon(color, moon_x, moon_y, moon_size):
    """
    Draw the Moon
    :param color: Moon color
    :param moon_x: X coordinate of the Moon
    :param moon_y: Y coordinate of the Moon
    :param moon_size: Moon radius
    :return: None
    """
    circle(screen, color, (moon_x, moon_y), moon_size)


def _draw_cloud(color, x, y, width, height):
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
    walls_color = (51, 26, 0)
    walls_x = x+ceil(0.1*width)
    walls_y = y+ceil(0.3*height)
    walls_width = ceil(0.8*width)
    walls_height = ceil(0.7*height)
    _draw_walls(walls_color, walls_x, walls_y, walls_width, walls_height)

    balcony_color = (26, 13, 0)
    balcony_x = x
    balcony_y = y + ceil(0.6 * height)
    balcony_width = width
    balcony_height = ceil(0.1 * height)
    _draw_balcony(balcony_color, balcony_x, balcony_y,
                  balcony_width, balcony_height)

    roof_color = (26, 13, 0)
    roof_x = x
    roof_y = y + ceil(0.2 * height)
    roof_width = width
    roof_height = ceil(0.1 * height)
    _draw_roof(roof_color, roof_x, roof_y, roof_width, roof_height)


def _draw_walls(color, x, y, width, height):
    rect(screen, color, (x, y, width, height))

    x_upper_windows = ceil(1.1 * x)
    y_upper_windows = y
    w = (width - ceil(0.1 * x) * 2) / 4 / 100
    width_upper_windows = ceil(60 * w)
    height_upper_windows = ceil(0.3 * height)
    distance_between_upper = ceil(110 * w)
    _draw_window((153, 102, 0), x_upper_windows, y_upper_windows,
                width_upper_windows, height_upper_windows, distance_between_upper, 4)

    x_lower_windows = ceil(1.3 * x)
    y_lower_windows = ceil(2 * y)
    w = (width - ceil(0.6 * x) * 2) / 3 / 100
    width_lower_windows = ceil(100 * w)
    height_lower_windows = ceil(0.2 * height)
    distance_between_lower = ceil(130 * w)
    _draw_window((230, 230, 0), x_lower_windows, y_lower_windows,
                 width_lower_windows, height_lower_windows, distance_between_lower, 3)


def _draw_window(color, x, y, width, height, distance_between, num_of_window):
    for _ in range(num_of_window):
        rect(screen, color, (x, y, width, height))
        x += distance_between


def _draw_balcony(color, x, y, width, height):

    rect(screen, color, (x, y, width, -height))

    partition_x = x
    partition_y = y
    width_partition_cube = width // 6
    height_partition = 2 * height

    for _ in range(6):
        rect(screen, color, (partition_x, partition_y,
                                   width_partition_cube, -height_partition), 20)
        partition_x += width_partition_cube


def _draw_roof(color, x, y, width, height):
    point_1 = (x + ceil(0.05 * width), y)
    point_2 = (x + (width - ceil(0.05 * width)), y)
    point_3 = (x + width, y + height)
    point_4 = (x, y + height)
    polygon(screen, color, [point_1,  point_2, point_3, point_4])

    rect(screen, color, (x+ceil(0.3*width), y,
                         ceil(0.1*width), -ceil(2*height)))


def draw_ghost(x, y, width, height):

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


draw_environment(900, 1000)
draw_house(50, 100, 500, 800)
draw_ghost(1, 1, 1, 1)
main()
