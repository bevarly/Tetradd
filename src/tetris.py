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

class Tetradd:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([450, 700])
        self.base_font = pygame.font.Font('Eight-Bit Madness.ttf', 32)
        self.answer_box = pygame.Rect(90, 50, 60, 30)
        self.equation_rect = pygame.Rect(20, 50, 60, 30)
        self.game_title = 'Tetradd'
        self.user_text = ''
        self.equation = ''
        self.str_sum = ''
        self.screenColor = (159, 226, 191)
        self.color_on = (237, 199, 250)
        self.color_off = (0, 0, 0)
        self.num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.num1 = random.choice(self.num_list)
        self.num2 = random.choice(self.num_list)
        self.equation = str(self.num1) + "+" + str(self.num2)
        self.sum = self.num1 + self.num2
        self.str_sum = str(self.sum)
        self.active = False
        self.x = 210
        self.y = 120  # starting blocks height
        self.CONSTANT_VEL = 5
        # addition
        self.rotation_angle = 0  # initial rotation angle
        self.user_correct = False
        self.running = True

    def event_list(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.answer_box.collidepoint(event.pos):
                        self.active = True
                    else:
                        self.active = False
                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[0:-1]
                        else:
                            self.user_text += event.unicode

            if self.str_sum == self.user_text:
                self.y += 1
                self.user_correct = True
                keys = pygame.key.get_pressed()
                if keys[K_ESCAPE]:
                    self.running = False
                    self.quit()
                if keys[K_DOWN] and self.y < 650:
                    self.y += self.CONSTANT_VEL
                if keys[K_LEFT] and self.x > 0:
                    self.x -= self.CONSTANT_VEL
                if keys[K_RIGHT] and self.x < 430:
                    self.x += self.CONSTANT_VEL
                if keys[K_SPACE]:
                    self.rotation_angle += math.pi / 2  # Rotate by 90 degrees
                if self.user_correct and self.y > 650:  # after each correct answer
                    self.user_text = ""
                    self.rotation_angle = 0
                    self.x = 210  # setting x and y for each correct answer
                    self.y = 120
                    self.num1 = random.choice(self.num_list)
                    self.num2 = random.choice(self.num_list)
                    self.equation = str(self.num1) + "+" + str(self.num2)
                    self.sum = self.num1 + self.num2
                    self.str_sum = str(self.sum)

            self.screen.fill(self.screenColor)
            pygame.draw.rect(self.screen, (114, 79, 169), pygame.Rect(0, 0, 450, 120))
            self.screen.blit(self.base_font.render(self.game_title, True, (255, 255, 255)), (173, 10))

            color = self.color_on if self.active else self.color_off
            pygame.draw.rect(self.screen, color, self.answer_box, 2)
            user_answer = self.base_font.render(self.user_text, True, (40, 253, 21))
            self.screen.blit(user_answer, (self.answer_box.x + 5, self.answer_box.y + 5))
            self.answer_box.w = user_answer.get_width() + 30

            pygame.draw.rect(self.screen, self.color_on, self.equation_rect, 2)
            equation_text = self.base_font.render(self.equation, True, (255, 255, 255))
            self.screen.blit(equation_text, (self.equation_rect.x + 5, self.equation_rect.y + 5))
            pygame.display.flip()

    def quit(self):
        self.running = False
        pygame.quit()

if __name__ == '__main__':
    t1 = Tetradd()
    t1.event_list()

