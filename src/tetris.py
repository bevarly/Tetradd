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
import time


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
        self.x = 210
        self.y = 120
        self.movement = 275

    def screenfill(self):
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

    def correct_pop(self): #correct popup
        message_on = True
        for t in range(10):
            text = " "
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

    def square_rect(self): #square shape
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x-2, self.y, 44, 44))
        pygame.draw.rect(self.screen, (253, 216, 53), (self.x, self.y+2, 40, 40))

    def mascot_rect(self): #dog goes into abyss
        if self.user_ans != "":
            doggy = pygame.draw.rect(self.screen, (114, 79, 169 ), (self.movement, 40, 80, 80))
            image = pygame.image.load('pixel-art-cute-fox-png-t3atin7a90wibunw.png')
            image = pygame.transform.scale(image, (doggy.height, doggy.width))
            self.screen.blit(image, doggy)





class Nums(Rects):

    def prob_nums(self):  #num generator
        window.num1 = random.choice(window.num_list)
        window.num2 = random.choice(window.num_list)
        window.question_string = str(window.num1) + "+" + str(window.num2)
        window.answer = window.num1 + window.num2
        window.str_sum = str(window.answer)

if __name__ == '__main__':
    pygame.init()
    window = Rects()
    rando = Nums()
    clock = pygame.time.Clock()
    y = 120
    x = 210
    CONSTANT_VEL = 5
    rotation_angle = 0
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
                        window.user_ans = window.user_ans[0:-1]  #allow to delete
                    else:
                        window.user_ans += event.unicode  #typ
        window.screenfill()
        window.answer_rect()
        window.square_rect()
        window.mascot_rect()
        if window.user_ans == window.str_sum:
            if window.y == 120:
                window.correct_pop()
            window.y += 1
            window.movement += 1
            user_correct = True
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                running = False
            if keys[K_DOWN] and y < 650:
                window.y += CONSTANT_VEL
            if keys[K_LEFT] and x > 0:
                window.x -= CONSTANT_VEL
            if keys[K_RIGHT] and x < 430:
                window.x += CONSTANT_VEL
            if keys[K_SPACE]:
                rotation_angle += math.pi / 2
            if user_correct and window.y >= 650:
                window.user_ans = ""
                rotation_angle = 0
                window.x = 210
                window.y = 120
                rando.prob_nums()
        window.num_rect()
        pygame.display.flip()
