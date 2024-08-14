import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра тир!')
icon = pygame.image.load("img/Без имени.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randrange(0, SCREEN_WIDTH - target_width)
target_y = random.randrange(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Счетчик попаданий
score = 0
font = pygame.font.Font(None, 36)  # Создаем шрифт для отображения счета

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем счетчик попаданий
                target_x = random.randrange(0, SCREEN_WIDTH - target_width)
                target_y = random.randrange(0, SCREEN_HEIGHT - target_height)

    # Отображаем мишень
    screen.blit(target_img, (target_x, target_y))

    # Отображаем счет
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))  # Белый текст
    screen.blit(score_text, (10, 10))  # Отображаем текст в левом верхнем углу

    pygame.display.update()

pygame.quit()
