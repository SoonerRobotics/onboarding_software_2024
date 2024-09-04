import random
import pygame
import sys
from pygame.locals import *

# Set up the window
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 1
BALL_SPEED = 1

# Initialize pygame
pygame.init()
fps = pygame.time.Clock()

# Set up the display
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('SCR Onboarding 2024 | TicTacToe')

class TicTacToe:
    def __init__(self):
        self.board = [0 for _ in range(9)]
        self.turn = 1
        self.winner = None

    def draw_grid(self):
        for i in range(1, 3):
            pygame.draw.line(window, (0, 0, 0), (i * WIDTH / 3, 0), (i * WIDTH / 3, HEIGHT), 5)
            pygame.draw.line(window, (0, 0, 0), (0, i * HEIGHT / 3), (WIDTH, i * HEIGHT / 3), 5)

    def draw_x(self, x, y):
        pygame.draw.line(window, (0, 0, 0), (x * WIDTH / 3, y * HEIGHT / 3), ((x + 1) * WIDTH / 3, (y + 1) * HEIGHT / 3), 5)
        pygame.draw.line(window, (0, 0, 0), ((x + 1) * WIDTH / 3, y * HEIGHT / 3), (x * WIDTH / 3, (y + 1) * HEIGHT / 3), 5)

    def draw_o(self, x, y):
        pygame.draw.circle(window, (0, 0, 0), (int((x + 0.5) * WIDTH / 3), int((y + 0.5) * HEIGHT / 3)), int(WIDTH / 9 - 5), 5)

    def check_winner(self):
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != 0:
                self.winner = self.board[i]
                return True
            if self.board[3 * i] == self.board[3 * i + 1] == self.board[3 * i + 2] != 0:
                self.winner = self.board[3 * i]
                return True
        if self.board[0] == self.board[4] == self.board[8] != 0:
            self.winner = self.board[0]
            return True
        if self.board[2] == self.board[4] == self.board[6] != 0:
            self.winner = self.board[2]
            return True
        return False
        
    def check_draw(self):
        return all([x != 0 for x in self.board])
    
    def make_move(self, x, y):
        if self.board[3 * y + x] == 0:
            self.board[3 * y + x] = self.turn
            self.turn = 3 - self.turn
            return True
        return False
    
    def get_move(self):
        if self.turn == 1:
            x, y = random.randint(0, 2), random.randint(0, 2)
            while not self.make_move(x, y):
                x, y = random.randint(0, 2), random.randint(0, 2)
        else:
            pass

    def draw(self):
        window.fill((255, 255, 255))
        self.draw_grid()
        for i in range(3):
            for j in range(3):
                if self.board[3 * j + i] == 1:
                    self.draw_x(i, j)
                elif self.board[3 * j + i] == 2:
                    self.draw_o(i, j)
        pygame.display.update()

ttt = TicTacToe()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            x, y = x // (WIDTH // 3), y // (HEIGHT // 3)
            ttt.make_move(x, y)
            if ttt.check_winner():
                print(f"Player {3 - ttt.turn} wins!")
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()

    ttt.draw()

    pygame.display.update()
    fps.tick(30)