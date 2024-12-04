import pygame
import time
import random
import pyttsx3
from datetime import datetime
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.say(text)
    engine.runAndWait()

pygame.init()
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

width = 600
height = 400
m = "Game Over! Press C to Play Again or Q to Quit"
display = pygame.display.set_mode((width, height))

pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake = 10
snake_speed = 13

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def score_display(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])


def draw_snake(snake, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, blue, [x[0], x[1], snake, snake])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    dx = 0
    dy = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(black)
            message
            message(m, red)
            speak(m)
            score_display(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake
                    dx = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += dx
        y += dy

        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, snake, snake])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake, snake_list)
        score_display(length_of_snake - 1)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
