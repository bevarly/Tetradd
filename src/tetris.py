import pygame
import random
from pygame.locals import(
    K_ESCAPE,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    QUIT,
)
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([450, 700])

width = 20
height = 20
screenColor = (159, 226, 191)
rectColor = (114, 79, 169)

x = 210
y = 118
CONSTANT_VEL = 5
running = True
while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        running = False
        break
    if keys[K_DOWN] and y < 650:
        y += CONSTANT_VEL
    if keys[K_LEFT] and x > 0:
        x -= CONSTANT_VEL
    if keys[K_RIGHT] and x < 430:
        x += CONSTANT_VEL
    y += 1
    if y > 650:
        y = 1
    screen.fill(screenColor)
    border = pygame.draw.rect(screen, (114, 79, 169), pygame.Rect(0, 0, 450, 120))

    # list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # tries = [1, 2, 3]
    # green = (0, 255, 0)
    # blue = (0, 0, 128)
    # num1 = random.choice(list)
    # num2 = random.choice(list)
    # sum = str(num1 + num2)
    # equation = num1, '+', num2
    # if y == 120:
    #     y -= 1
    #     for x in tries:
    #         font = pygame.font.Font('freesansbold.ttf', 32)
    #         text = font.render(str(equation), True, green, blue)
    #         screen.blit(text, border)



    pygame.draw.rect(screen, rectColor, pygame.Rect(x, y, width, height))
    pygame.display.flip()
pygame.quit()

