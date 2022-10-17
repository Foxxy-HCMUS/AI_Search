import pygame
from math import sin, cos, radians

pygame.init()
wn = pygame.display.set_mode((600, 600))

r = 100
a = 300
b = 200

def x_y(r, i, a, b):
   return (int(r * cos(radians(i)) + a), int(r * sin(radians(i)) + b))

clock = pygame.time.Clock()
for i in range(0, 360, 2):
   clock.tick(30)
pygame.draw.line(wn, (255, 255, 255), x_y(r, i, a, b), x_y(r, i + 1, a, b), 2)
pygame.display.update()