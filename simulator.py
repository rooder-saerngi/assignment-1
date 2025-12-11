import pygame
import sys
import random

pygame.init()

WIDTH,HEIGHT = 1280 , 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Traffic Simulator")
pygame.mouse.set_visible(0)

bg = pygame.image.load("Road.png")
#Making sure that the exit button works

clock = pygame.time.Clock()
FPS = 60
while True:
    for event in pygame.event.get():

        screen.blit(bg, (0, 0))

        pygame.display.update()

        clock.tick(FPS)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
