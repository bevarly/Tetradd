import pygame
import random
from pygame.locals import (
    K_ESCAPE,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    QUIT,
    K_SPACE
)
import math
from rects import Rects


def prob_nums():  #num generator
    window.num1 = random.choice(window.num_list)
    window.num2 = random.choice(window.num_list)
    window.question_string = str(window.num1) + "+" + str(window.num2)
    window.answer = window.num1 + window.num2
    window.str_sum = str(window.answer)


class Blocks:
    def __init__(self, screen, side, down):
        self.screen = screen
        self.x = side
        self.y = down
        self.CONSTANT_VEL = 5
        self.movement = 275
        self.rotation_angle = 0.0
        self.SHAPES = []
        self.SHAPES.append(self.square)
        self.SHAPES.append(self.i_shape)
        self.SHAPES.append(self.t_shape)
        self.SHAPES.append(self.l_shape)
        self.current_shape = None
        self.fallen_shapes = []

    def change_pos(self):
        self.y += 1
        if self.y < 650:
            keys = pygame.key.get_pressed()
            if keys[K_DOWN] and self.y < 650:
                self.y += self.CONSTANT_VEL
            if keys[K_LEFT] and self.x > 0:
                self.x -= self.CONSTANT_VEL
            if keys[K_RIGHT] and self.x < 430:
                self.x += self.CONSTANT_VEL
            if keys[K_SPACE]:
                self.rotation_angle += math.pi / 2
        else:
            self.y = 649

    def blocks_spawn(self):
        spawn = random.choice(self.SHAPES)
        self.current_shape = spawn
        spawn()
        return self.current_shape

    def fallen_shapes(self):


    def square(self):
        #square
        outline = pygame.draw.rect(self.screen, (0, 0, 0), (self.x - 1, self.y, 42, 43))
        base = pygame.draw.rect(self.screen, (253, 216, 53), (self.x, self.y + 1, 40, 41))
        return outline, base

    def l_shape(self):
        outline = pygame.draw.polygon(self.screen, (0, 0, 0),
                                      ([self.x, self.y], [self.x, self.y + 43], [self.x + 35, self.y + 43],
                                       [self.x + 35, self.y + 28], [self.x + 13, self.y + 28], [self.x + 13, self.y]))

        base = pygame.draw.polygon(self.screen, (54, 103, 244),
                                   ([self.x + 2, self.y + 2], [self.x + 2, self.y + 41], [self.x + 33, self.y + 41],
                                    [self.x + 33, self.y + 30], [self.x + 11, self.y + 30], [self.x + 11, self.y + 2]))
        return outline, base

    def t_shape(self):
        #T shape
        outline = pygame.draw.polygon(self.screen, (0, 0, 0), ([self.x - 7, self.y], [self.x - 7, self.y + 13],
                                                               [self.x + 10, self.y + 13], [self.x + 10, self.y + 40],
                                                               [self.x + 23, self.y + 40],
                                                               [self.x + 23, self.y + 13], [self.x + 40, self.y + 13],
                                                               [self.x + 40, self.y]))
        base = pygame.draw.polygon(self.screen, (223, 29, 29), ([self.x - 5, self.y + 2], [self.x - 5, self.y + 10],
                                                                [self.x + 12, self.y + 10], [self.x + 12, self.y + 38],
                                                                [self.x + 21, self.y + 38],
                                                                [self.x + 21, self.y + 10], [self.x + 38, self.y + 10],
                                                                [self.x + 38, self.y + 2]))
        return outline, base

    def i_shape(self):
        #I shape
        outline = pygame.draw.polygon(self.screen, (0, 0, 0),
                                      ([self.x - 3, self.y], [self.x - 3, self.y + 50], [self.x + 10, self.y + 50],
                                       [self.x + 10, self.y]))
        base = pygame.draw.polygon(self.screen, (225, 12, 143),
                                   ([self.x - 1, self.y + 2], [self.x - 1, self.y + 48], [self.x + 8, self.y + 48],
                                    [self.x + 8, self.y + 2]))
        return outline, base


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([450, 700])
    x = 210
    y = 120
    window = Rects(screen)
    bottom_shapes = []
    move = Blocks(screen, x, y)
    shapes = Blocks(screen, x, y)

    #shapes
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if window.answer_box.collidepoint(event.pos):
                    window.active = True
                else:
                    window.active = False
            if event.type == pygame.KEYDOWN:
                if window.active:
                    if event.key == pygame.K_BACKSPACE:
                        window.user_ans = window.user_ans[0:-1]  #allows to delete
                    else:
                        window.user_ans += event.unicode  #typing method
        window.screen_fill()
        window.answer_rect()
        # shape spawn
        if window.user_ans == window.str_sum:
            if shapes.y == 120:
                window.correct_pop()
                shapes.blocks_spawn()
            shapes.current_shape()
            user_correct = True
            shapes.change_pos()
            if user_correct and shapes.y >= 649:
                shapes.y = 120
                window.user_ans = ""
                rotation_angle = 0
                prob_nums()

        window.num_rect()
        pygame.display.flip()
