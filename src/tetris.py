import pygame
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
rectColor = (114, 79, 128)

x = 225
y = 1
vel = 5
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
        y += vel
    if keys[K_LEFT] and x > 0:
        x -= vel
    if keys[K_RIGHT] and x < 430:
        x += vel

    y += 1
    if y > 650:
        y = 1

    screen.fill(screenColor)
    pygame.draw.rect(screen, rectColor, pygame.Rect(x, y, width, height))
    pygame.display.flip()
pygame.quit()

