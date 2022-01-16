import pygame
import random
from copy import copy, deepcopy


class MainWindow:
    def __init__(self, width, height, fps):
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill((100, 100, 100))
        for i in range(self.width // 15):
            pygame.draw.line(self.screen, (0, 0, 0), [i * 15, 0], [i * 15, self.height - 100])
        pygame.display.update()
        for i in range((self.height - 100) // 15 + 1):
            pygame.draw.line(self.screen, (0, 0, 0), [0, i * 15], [self.width, i * 15])
        self.squares = [[0 for j in range(width // 15)] for i in range(height // 15)]
        self.coords = [[1, 1],
                       [1, 0],
                       [1, -1],
                       [0, 1],
                       [0, -1],
                       [-1, 1],
                       [-1, 0],
                       [-1, -1]]
        self.button = Button(100, 50, "Start")
        self.button.drawing(self.screen, 400, 625)

    def neighbours(self, x_, y_, squares_2_):
        count = 0
        for i in self.coords:
            if 0 <= x_ + i[0] < self.width // 15 and 0 <= y_ + i[1] < self.height // 15:
                if squares_2_[y_ + i[1]][x_ + i[0]]:
                    count += 1
        return count

    def matrix(self):
        squares_2 = deepcopy(self.squares)
        for x in range(self.width // 15):
            for y in range(self.height // 15):
                if self.squares[y][x]:
                    if self.neighbours(x, y, squares_2) != 2 and self.neighbours(x, y, squares_2) != 3:
                        self.squares[y][x] = 0
                else:
                    if self.neighbours(x, y, squares_2) == 3:
                        self.squares[y][x] = 1

    def drawing(self):
        for x in range(self.width // 15):
            for y in range((self.height - 100) // 15):
                if self.squares[y][x]:
                    pygame.draw.rect(self.screen, (255, 69, 0), (x * 15 + 1, y * 15 + 1, 14, 14))
                else:
                    pygame.draw.rect(self.screen, (100, 100, 100), (x * 15 + 1, y * 15 + 1, 14, 14))

    def start(self):
        pygame.init()
        pygame.display.set_caption("Game of life")
        clock = pygame.time.Clock()
        flag = True
        flag_2 = False
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[1] < self.height:
                        self.squares[event.pos[1] // 15][event.pos[0] // 15] = 1
                    if 400 <= event.pos[0] <= 400 + 100:
                        if 625 <= event.pos[1] <= 625 + 50:
                            if flag_2:
                                self.button = Button(100, 50, "Start")
                                self.button.drawing(self.screen, 400, 625)
                                flag_2 = False
                            else:
                                self.button = Button(100, 50, "Stop")
                                self.button.drawing(self.screen, 400, 625)
                                flag_2 = True
            clock.tick(self.fps)
            self.drawing()
            if flag_2:
                self.matrix()
            pygame.display.update()
        pygame.quit()


class Button:
    def __init__(self, is_width, is_height, text):
        self.is_width = is_width
        self.is_height = is_height
        self.text = text

    def drawing(self, screen, x, y):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(screen, (255, 99, 71), (x, y, self.is_width, self.is_height))
        pygame.font.init()
        font_type = pygame.font.SysFont('arial', 36)
        text_2 = font_type.render(self.text, True, (255, 255, 255))
        screen.blit(text_2, (410, 635))


life_of_game = MainWindow(900, 700, 5)
life_of_game.start()
