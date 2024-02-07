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
base_font = pygame.font.Font('Eight-Bit Madness.ttf', 32)
answer_box = pygame.Rect(90, 50, 60, 30)
equation_rect = pygame.Rect(20, 50, 60, 30)
game_title = 'Tetradd'
user_text = ''
equation = ''
str_sum = ''


width = 20
height = 20
screenColor = (159, 226, 191)
rectColor = (114, 79, 169)
color_on = (0, 0, 0)
color_off = (237, 199, 250)
color = color_off


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num1 = random.choice(num_list)
num2 = random.choice(num_list)
equation = str(num1) + "+" + str(num2)
sum = num1 + num2
str_sum = str(sum)

active = False

x = 210
y = 118
CONSTANT_VEL = 5
running = True
while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if answer_box.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                else:
                    user_text += event.unicode
    y += 0
    user_correct = False
    if str_sum == user_text:
        y += 1
        user_correct = True
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
        if user_correct == True and y > 650:
            user_text = ''
            y = 118
            num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            num1 = random.choice(num_list)
            num2 = random.choice(num_list)
            equation = str(num1) + "+" + str(num2)
            sum = num1 + num2
            str_sum = str(sum)


    screen.fill(screenColor)
    border = pygame.draw.rect(screen, (114, 79, 169), pygame.Rect(0, 0, 450, 120))
    text_surface = base_font.render(game_title, True, (255, 255, 255))
    screen.blit(text_surface, (173, 10))

    if active:
        color = color_on
    else:
        color = color_off
    input_box = pygame.draw.rect(screen, color, answer_box, 2)
    user_answer = base_font.render(user_text, True, (40, 253, 21))
    screen.blit(user_answer, (input_box.x + 5, input_box.y + 5))
    answer_box.w = user_answer.get_width() + 30

    equation_box = pygame.draw.rect(screen, color_on, equation_rect, 2)
    equation_text = base_font.render(equation, True, (255, 255, 255))
    screen.blit(equation_text, (equation_box.x + 5, equation_box.y + 5))

    pygame.draw.rect(screen, rectColor, pygame.Rect(x, y, width, height))
    pygame.display.flip()
pygame.quit()

