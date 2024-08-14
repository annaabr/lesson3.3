import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра тир!')
icon = pygame.image.load("img/Без имени.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load(("img/target.png"))
target_width = 50
target_height = 50

target_x = random.randrange(0, SCREEN_WIDTH - target_width)
target_y = random.randrange(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    pass

pygame.quit()
