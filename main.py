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

# Начальная позиция цели
target_x = random.randrange(0, SCREEN_WIDTH - target_width)
target_y = random.randrange(0, SCREEN_HEIGHT - target_height)

# Направление и скорость
target_dx = random.choice([-1, 1]) * random.uniform(0.03, 0.07)
target_dy = random.choice([-1, 1]) * random.uniform(0.03, 0.07)

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
                # Перемещение цели в случайную точку
                target_x = random.randrange(0, SCREEN_WIDTH - target_width)
                target_y = random.randrange(0, SCREEN_HEIGHT - target_height)
                target_dx = random.choice([-1, 1]) * random.uniform(0.03, 0.07)
                target_dy = random.choice([-1, 1]) * random.uniform(0.03, 0.07)

    # Обновляем позицию цели
    target_x += target_dx
    target_y += target_dy

    # Проверка выхода за пределы экрана
    if target_x < 0 or target_x > SCREEN_WIDTH - target_width:
        target_dx = -target_dx  # Меняем направление по оси X
    if target_y < 0 or target_y > SCREEN_HEIGHT - target_height:
        target_dy = -target_dy  # Меняем направление по оси Y

    # Отображаем мишень
    screen.blit(target_img, (target_x, target_y))

    # Отображаем счет
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))  # Белый текст
    screen.blit(score_text, (10, 10))  # Отображаем текст в левом верхнем углу

    pygame.display.update()

pygame.quit()