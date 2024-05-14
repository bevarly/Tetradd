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


class Rects:
    def __init__(self):
        self.screen = pygame.display.set_mode([450, 700])
        self.colors = (159, 226, 191)
        self.fonts = pygame.font.Font('Eight-Bit Madness.ttf', 32)
        self.equation_rect = pygame.Rect(20, 50, 60, 30)
        #user_text box active indication
        self.color_on = (237, 199, 250)
        self.color_off = (0, 0, 0)
        self.answer_box = pygame.Rect(90, 50, 60, 30)
        self.active = True
        self.user_ans = ""
        #rando num generator
        self.num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.num1 = random.choice(self.num_list)
        self.num2 = random.choice(self.num_list)
        self.question_string = str(self.num1) + "+" + str(self.num2)
        self.answer = self.num1 + self.num2
        self.str_sum = str(self.answer)

    def screen_fill(self):
        self.screen.fill(self.colors)
        pygame.draw.rect(self.screen, (114, 79, 169), pygame.Rect(0, 0, 450, 120))
        self.screen.blit(self.fonts.render('Tetradd', True, (255, 255, 255)), (173, 10))

    def answer_rect(self):  #user input box
        color = self.color_on if self.active else self.color_off
        pygame.draw.rect(self.screen, color, self.answer_box, 2)
        user_answer = self.fonts.render(self.user_ans, True, (40, 253, 21))
        self.screen.blit(user_answer, (self.answer_box.x + 5, self.answer_box.y + 5))
        self.answer_box.w = user_answer.get_width() + 30

    def num_rect(self):  #question box
        pygame.draw.rect(self.screen, self.color_on, self.equation_rect, 2)
        equation_text = self.fonts.render(self.question_string, True, (255, 255, 255))
        self.screen.blit(equation_text, (self.equation_rect.x + 5, self.equation_rect.y + 5))
        return self.str_sum

    def correct_pop(self):  #correct popup
        message_on = True
        for t in range(10):
            if message_on:
                text = "CORRECT!"
            else:
                text = ""
            message_on = not message_on
            self.screen.fill((0, 0, 0), (145, 295, 160, 30))
            self.screen.blit(self.fonts.render(text, True, (240, 80, 226)), (165, 300))
            pygame.time.delay(100)
            pygame.display.flip()
            pygame.time.delay(0)

    #
    # def mascot_rect(self):  #dog goes into abyss, work in progress
    #     if window.active:
    #         doggy = pygame.draw.rect(self.screen, (114, 79, 169), (self.movement, 40, 80, 80))
    #         image = pygame.image.load('pixel-art-cute-fox-png-t3atin7a90wibunw.png')
    #         image = pygame.transform.scale(image, (doggy.height, doggy.width))
    #         self.screen.blit(image, doggy)


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

    def change_pos(self):
        self.y += 1
        keys = pygame.key.get_pressed()
        if keys[K_DOWN] and self.y < 650:
            self.y += self.CONSTANT_VEL
        if keys[K_LEFT] and self.x > 0:
            self.x -= self.CONSTANT_VEL
        if keys[K_RIGHT] and self.x < 430:
            self.x += self.CONSTANT_VEL
        if keys[K_SPACE]:
            self.rotation_angle += math.pi / 2

    def blocks_spawn(self):
        spawn = random.choice(self.SHAPES)
        self.current_shape = spawn
        spawn()
        return self.current_shape

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
    x = 120
    y = 210
    window = Rects()
    move = Blocks(window.screen, y, x)
    shapes = Blocks(window.screen, y, x)


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
            if y == 210:
                window.correct_pop()
                shapes.blocks_spawn()
            y += 1
            shapes.current_shape()
            user_correct = True
            shapes.change_pos()
            if user_correct and y >= 650:
                window.user_ans = ""
                rotation_angle = 0
                y = 210
                prob_nums()

        window.num_rect()
        pygame.display.flip()
