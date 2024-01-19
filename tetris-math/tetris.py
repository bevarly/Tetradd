import time
import pygame
from pygame.locals import(
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()

screen = pygame.display.set_mode([450, 700])
x = 200
y = 1
width = 20
height = 20
vel = 15
screen.fill((159, 226, 191))
color = (114, 79, 128)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and y>0:
            color = (159, 226, 191)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
            y+= vel
            color = (114, 79, 128)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
            keys_not = pygame.K_END
        if keys[pygame.K_UP] and y>0:
            color = (159, 226, 191)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
            y-= vel
            color = (114, 79, 128)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
        if keys[pygame.K_LEFT] and x>0:
            color = (159, 226, 191)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
            x-= vel
            color = (114, 79, 128)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
        if keys[pygame.K_RIGHT] and x>0:
            color = (159, 226, 191)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
            x+= vel
            color = (114, 79, 128)
            pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    pygame.display.flip()
pygame.quit()
