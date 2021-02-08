import pygame
from pygame.draw import *
from random import randint

# It is pygame initialization
pygame.init()

# Display settings
FPS = 2
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Point counter
counter = 0

# Text name
font_name = pygame.font.match_font("arial")


def main():
    """
    It is the main game loop
    """
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    point_counter(click(event.pos))
        draw_point_counter(screen, counter, 30, 500, 50)
        new_ball()
        pygame.display.update()
        screen.fill(BLACK)


def new_ball():
    """
    It draws random circle at random point
    """
    global x, y, r
    x = randint(SCREEN_WIDTH//100*10, SCREEN_WIDTH//100*90)
    y = randint(SCREEN_HEIGHT//100*10, SCREEN_HEIGHT//100*90)
    r = randint(SCREEN_WIDTH//100*2, SCREEN_WIDTH//100*6)
    color = COLORS[randint(0, 5)]
    pygame.draw.circle(screen, color, (x, y), r)


def click(event_pos):
    """
    It return True if player clicks in a circle
    :param event: event.pos
    :return: True or False
    """
    clicked_pos_x, clicked_pos_y = event_pos
    res = abs((clicked_pos_x**2 + clicked_pos_y**2)**0.5 - (x**2 + y**2)**0.5)
    if res < r:
        return True


def point_counter(click_result):
    """
    It counts the game points
    :param click_result: It is return of click function
    :return: counter
    """
    global counter
    if click_result == True:
        counter += 5
    return counter


def draw_point_counter(surf, text, size, x_pos, y_pos):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(str(text), True, WHITE)
    surf.blit(text_surface, (x_pos, y_pos))


main()

# It get out of program
pygame.quit()
