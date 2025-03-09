import pygame
from pygame import Vector2
import sys
import random


class Fruit:
    def __init__(self):
        self.x = random.randint(1, cell_number - 1)
        self.y = random.randint(1, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (242, 68, 41), fruit_rect)

    def move(self):
        self.x = random.randint(1, cell_number - 1)
        self.y = random.randint(1, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class Snake:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.direction = Vector2(1, 0)

    def draw(self):
        for segment in self.body:
            seg_rect = pygame.Rect(segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (73, 91, 245), seg_rect)

    def move(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

    def add_seg(self):
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + Vector2(self.direction))
        self.body = body_copy


def end_game():
    pygame.quit()
    sys.exit()


pygame.init()
cell_size = 20
cell_number = 30
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
fruit = Fruit()
snake = Snake()
SCREEN_UPDATE = pygame.USEREVENT
EAT_FRUIT = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
print(fruit.pos)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game()
        if event.type == SCREEN_UPDATE:
            snake.move()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake.direction != (0, 1):
                    snake.direction = (0, -1)
            if event.key == pygame.K_DOWN:
                if snake.direction != (0, -1):
                    snake.direction = (0, 1)
            if event.key == pygame.K_RIGHT:
                if snake.direction != (-1, 0):
                    snake.direction = (1, 0)
            if event.key == pygame.K_LEFT:
                if snake.direction != (1, 0):
                    snake.direction = (-1, 0)
    if snake.body[0] == fruit.pos:
        fruit.move()
        snake.add_seg()
    for seg in snake.body[1:]:
        if seg == snake.body[0]:
            end_game()
    if not 0 <= snake.body[0].x <= cell_number - 1 or not 0 <= snake.body[0].y <= cell_number - 1:
        pygame.quit()
        sys.exit()
    screen.fill((161, 235, 52))
    fruit.draw()
    snake.draw()
    pygame.display.update()
    clock.tick(60)
