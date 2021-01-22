import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (209, 224, 224), (0, 0 ,400 ,400))
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (150, 180), 20)
circle(screen, (255, 0, 0), (250, 180), 15)
circle(screen, (0, 0, 0), (150, 180), 9)
circle(screen, (0, 0, 0), (250, 180), 7)
rect(screen, (0, 0, 0), (150, 245 ,100 ,25))
rect(screen, (0, 0, 0), (150, 245 ,100 ,25))
rect(screen, (0, 0, 0), (150, 245 ,100 ,25))
line(screen, (0, 0, 0), (90,130), (190,170), 10)
line(screen, (0, 0, 0), (310,120), (230,170), 14)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()