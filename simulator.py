import pygame
import sys

from pygame.examples.moveit import WIDTH, HEIGHT

pygame.init()

WIDTH,HEIGHT = 1280 , 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Traffic Simulator")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
