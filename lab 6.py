import pygame
from random import randint

# It is pygame initialization
pygame.init()

# Display settings
FPS = 1
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

# Point counter settings
point_counter_x = 30
point_counter_y = 30
text_size = 40

# Create new counter every game
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
        new_ball()
        pygame.display.update()
        screen.fill(BLACK)


def new_ball():
    """
    It draws random circle at random point
    """
    global x, y, r
    x = randint(SCREEN_WIDTH//100*30, SCREEN_WIDTH//100*70)
    y = randint(SCREEN_HEIGHT//100*30, SCREEN_HEIGHT//100*70)
    r = randint(SCREEN_WIDTH//100*2, SCREEN_WIDTH//100*6)
    color = COLORS[randint(0, 5)]
    variant = randint(1, 8)
    variant_back = randint(1, 3)
    kontact_position = 0
    speed_2_coordinate = 12
    speed_1_coordinate = 8

    for i in range(300):
        screen.fill(BLACK)
        draw_point_counter(screen, counter, text_size,
                           point_counter_x, point_counter_y)
        if x-r > 0 and x+r < SCREEN_WIDTH and y-r > 0 and y+r < SCREEN_HEIGHT:
            if variant == 1:
                y -= speed_1_coordinate
            elif variant == 2:
                y -= speed_2_coordinate
                x += speed_2_coordinate
            elif variant == 3:
                x += speed_1_coordinate
            elif variant == 4:
                y += speed_2_coordinate
                x += speed_2_coordinate
            elif variant == 5:
                y += speed_1_coordinate
            elif variant == 6:
                y += speed_2_coordinate
                x -= speed_2_coordinate
            elif variant == 7:
                x -= speed_1_coordinate
            elif variant == 8:
                y -= speed_2_coordinate
                x -= speed_2_coordinate
        pygame.draw.circle(screen, color, (x, y), r)
        pygame.display.update()


    if y - r <= 0:
        kontact_position = 1
    elif x + r >= SCREEN_WIDTH:
        kontact_position = 2
    elif y + r >= SCREEN_HEIGHT:
        kontact_position = 3
    elif x - r <= 0:
        kontact_position = 4


    if kontact_position > 0:
        for i in range(200):
            screen.fill(BLACK)
            draw_point_counter(screen, counter, text_size,
                               point_counter_x, point_counter_y)
            if x - r >= -5 and x + r <= SCREEN_WIDTH+5 and y - r >= -5 and y + r <= SCREEN_HEIGHT+5:
                if kontact_position == 1:
                    if variant_back == 1:
                        y += speed_2_coordinate
                        x -= speed_2_coordinate
                    if variant_back == 2:
                        y += speed_1_coordinate
                    if variant_back == 3:
                         y += speed_2_coordinate
                         x += speed_2_coordinate
                if kontact_position == 2:
                    if variant_back == 1:
                        y -= speed_2_coordinate
                        x -= speed_2_coordinate
                    if variant_back == 2:
                        x -= speed_1_coordinate
                    if variant_back == 3:
                        y += speed_2_coordinate
                        x -= speed_2_coordinate
                if kontact_position == 3:
                    if variant_back == 1:
                        y -= speed_2_coordinate
                        x += speed_2_coordinate
                    if variant_back == 2:
                        y -= speed_1_coordinate
                    if variant_back == 3:
                        y -= speed_2_coordinate
                        x -= speed_2_coordinate
                if kontact_position == 4:
                    if variant_back == 1:
                        y += speed_2_coordinate
                        x += speed_2_coordinate
                    if variant_back == 2:
                        x += speed_1_coordinate
                    if variant_back == 3:
                        y -= speed_2_coordinate
                        x += speed_2_coordinate
            pygame.draw.circle(screen, color, (x, y), r)
            pygame.display.update()

def click(event_pos):
    """
    It return True if player clicks in a circle
    :param event_pos: event.pos
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
    """
    It paints the point counter on a display
    :param surf: Display surface
    :param text: Text for paint
    :param size: Text size
    :param x_pos: Left point of text rect
    :param y_pos: Upper point of text rect
    """
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(str(text), True, WHITE)
    surf.blit(text_surface, (x_pos, y_pos))


main()

# It get out of program
pygame.quit()
