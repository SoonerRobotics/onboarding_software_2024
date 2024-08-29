import random
import pygame
import sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()

# Globals
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 5
BALL_SPEED = 5
BALL_ACCELERATION = 1.1

# Set up the display
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('SCR Onboarding 2024 | Pong')

# A basic point structure
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define the ball class
class Ball:
    def __init__(self, position, radius, color):
        self.position = position
        self.velocity = Point(random.choice([-1, 1]) * BALL_SPEED, random.choice([-1, 1]) * BALL_SPEED)
        self.radius = radius
        self.color = color

    def draw(self, canvas):
        pygame.draw.circle(canvas, self.color, [self.position.x, self.position.y], self.radius, 0)

    def move(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

    def bounce(self):
        self.velocity.x = -self.velocity.x * BALL_ACCELERATION # :3
        self.velocity.y = random.choice([-1, 1]) * BALL_SPEED

    def checkCollision(self, paddle_left, paddle_right):
        # Check the paddles
        if paddle_left.is_colliding(self) or paddle_right.is_colliding(self):
            self.bounce()

        # Check the walls
        if self.position.y - self.radius <= 0 or self.position.y + self.radius >= HEIGHT:
            self.velocity.y = -self.velocity.y

        if self.position.x - self.radius <= 0 or self.position.x + self.radius >= WIDTH:
            self.velocity.x = -self.velocity.x

    def wall_index(self):
        # Check if the ball is hitting the left wall, if so return 0
        if self.position.x - self.radius <= 0:
            return 0

        # Check if the ball is hitting the right wall, if so return 1
        if self.position.x + self.radius >= WIDTH:
            return 1

        # If the ball is not hitting any wall+
        return -1

# Define the paddle class
class Paddle:
    def __init__(self, position, width, height, color):
        self.position = position
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        pygame.draw.polygon(canvas, self.color, [[self.position.x - self.width/2, self.position.y - self.height/2], [self.position.x - self.width/2, self.position.y + self.height/2], [self.position.x + self.width/2, self.position.y + self.height/2], [self.position.x + self.width/2, self.position.y - self.height/2]], 0)

    def move(self, direction):
        self.position.y += direction

        if self.position.y - self.height / 2 < 0:
            self.position.y = self.height / 2

        if self.position.y + self.height / 2 > HEIGHT:
            self.position.y = HEIGHT - self.height / 2

    def is_colliding(self, ball):
        return ball.position.x - ball.radius <= self.position.x + self.width / 2 and ball.position.x + ball.radius >= self.position.x - self.width / 2 and ball.position.y - ball.radius <= self.position.y + self.height / 2 and ball.position.y + ball.radius >= self.position.y - self.height / 2


class Pong:
    def __init__(self):
        self.ball = Ball(Point(WIDTH/2, HEIGHT/2), BALL_RADIUS, (255, 255, 255))
        self.paddle_left = Paddle(Point(10, HEIGHT/2), 10, 60, (135, 206, 235))
        self.paddle_right = Paddle(Point(WIDTH - 10, HEIGHT/2), 10, 60, (76, 0, 76))

        self.score = [0, 0]

    def update(self):
        self.ball.move()
        self.ball.checkCollision(self.paddle_left, self.paddle_right)
        self.ai()

        if self.ball.wall_index() == 0:
            self.reset()
            self.score[1] += 1
            print("Player 2 wins!")

        if self.ball.wall_index() == 1:
            self.reset()
            self.score[0] += 1
            print("Player 1 wins!")

        pygame.display.set_caption('SCR Onboarding 2024 | Pong ({} - {})'.format(self.score[0], self.score[1]))

    def draw(self, canvas):
        canvas.fill((0, 0, 0))
        self.ball.draw(canvas)
        self.paddle_left.draw(canvas)
        self.paddle_right.draw(canvas)

    def movePaddle(self, direction):
        self.paddle_left.move(direction)

    def ai(self):
        if self.ball.position.y < self.paddle_right.position.y:
            self.paddle_right.move(-10)

        if self.ball.position.y > self.paddle_right.position.y:
            self.paddle_right.move(10)

    def reset(self):
        self.ball = Ball(Point(WIDTH/2, HEIGHT/2), BALL_RADIUS, self.ball.color)
        self.paddle_left = Paddle(Point(10, HEIGHT/2), 10, 60, self.paddle_left.color)
        self.paddle_right = Paddle(Point(WIDTH - 10, HEIGHT/2), 10, 60, self.paddle_right.color)


pong = Pong()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[K_UP]:
        pong.movePaddle(-10)

    if keys[K_DOWN]:
        pong.movePaddle(10)

    pong.update()
    pong.draw(window)

    pygame.display.update()
    fps.tick(30)
