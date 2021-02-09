import pygame
from random import randint

# It is pygame initialization
pygame.init()

# Display settings
FPS = 30
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
    global x, y, r, color, variant, variant_back, x_forward, y_forward, x_backward, y_backward, back_flag
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        new_ball()
        for i in range(400):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        point_counter(click(event.pos, x, y))
            screen.fill(BLACK)
            draw_point_counter(screen, counter, text_size,
                               point_counter_x, point_counter_y)
            if y - r <= 5 or x + r >= SCREEN_WIDTH - 5 or y + r >= SCREEN_HEIGHT - 5 or x - r <= 5:
                back_flag = True
                if y - r <= 5:
                    variant = 1
                elif x + r >= SCREEN_WIDTH - 5:
                    variant = 2
                elif y + r >= SCREEN_HEIGHT - 5:
                    variant = 3
                elif x - r <= 5:
                    variant = 4
                variant_back = randint(1, 2)
                x_backward, y_backward = randint(1, 6), randint(1, 6)

            if variant == 1:
                if not back_flag:
                    x += x_forward
                    y -= y_forward
                else:
                    if variant_back == 1:
                        x -= x_backward
                        y += y_backward
                    elif variant_back == 2:
                        x += x_backward
                        y += y_backward

            elif variant == 2:
                if not back_flag:
                    x += x_forward
                    y += y_forward
                else:
                    if variant_back == 1:
                        x -= x_backward
                        y -= y_backward
                    if variant_back == 2:
                        x -= x_backward
                        y += y_backward

            elif variant == 3:
                if not back_flag:
                    x -= x_forward
                    y += y_forward
                else:
                    if variant_back == 1:
                        x += x_backward
                        y -= y_backward
                    if variant_back == 2:
                        x -= x_backward
                        y -= y_backward

            elif variant == 4:
                if not back_flag:
                    x -= x_forward
                    y -= y_forward
                else:
                    if variant_back == 1:
                        x += x_backward
                        y += y_backward
                    if variant_back == 2:
                        x += x_backward
                        y -= y_backward
            pygame.draw.circle(screen, color, (x, y), r)
            pygame.display.update()
        pygame.display.update()
        screen.fill(BLACK)


def new_ball():
    """
    It draws random circle at random point and move him
    """
    global x, y, r, color, variant, variant_back, x_forward, y_forward, x_backward, y_backward, back_flag
    x = randint(SCREEN_WIDTH//100*10, SCREEN_WIDTH//100*90)
    y = randint(SCREEN_HEIGHT//100*10, SCREEN_HEIGHT//100*90)
    r = randint(SCREEN_WIDTH//100*2, SCREEN_WIDTH//100*6)
    color = COLORS[randint(0, 5)]
    variant = randint(1, 4)
    variant_back = randint(1, 2)
    x_forward, y_forward = 1, 1
    x_backward, y_backward = 1, 1
    back_flag = False


def click(event_pos, true_x, true_y):
    """
    It return True if player clicks in a circle
    :param event_pos: event.pos
    :return: True or False
    """
    clicked_pos_x, clicked_pos_y = event_pos
    res = abs((clicked_pos_x**2 + clicked_pos_y**2)**0.5 - (true_x**2 + true_y**2)**0.5)
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
