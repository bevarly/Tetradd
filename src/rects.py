import pygame, random
class Rects:
    def __init__(self, screen):
        self.screen = screen
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