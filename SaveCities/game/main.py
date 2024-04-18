import pygame
import sys
from gui.colors import *
pygame.init()

# Основные параметры экрана
screen_width, screen_height = 1000, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Save Cities")

# Шрифты
font = pygame.font.SysFont(None, 55)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    while True:
        screen.fill(white)
        draw_text("Save Cities", font, black, screen, 280, 20)

        mx, my = pygame.mouse.get_pos()

        button_start = pygame.Rect(300, 100, 200, 50)
        button_instructions = pygame.Rect(300, 200, 200, 50)
        button_quit = pygame.Rect(300, 300, 200, 50)

        if button_start.collidepoint((mx, my)):
            if click:
                game()  # Игра начнется здесь
        if button_instructions.collidepoint((mx, my)):
            if click:
                instructions()  # Отобразить инструкции
        if button_quit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, black, button_start)
        draw_text("Start", font, white, screen, 370, 110)
        pygame.draw.rect(screen, black, button_instructions)
        draw_text("Instructions", font, white, screen, 305, 210)
        pygame.draw.rect(screen, black, button_quit)
        draw_text("Quit", font, white, screen, 370, 310)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)

def game():
    running = True
    while running:
        screen.fill(white)

        # Рисуем реку
        pygame.draw.ellipse(screen, blue, pygame.Rect(25, 25, 950, 600), width=50)

        # Рисуем города
        city_positions = [(250, 250), (650, 150), (250, 400), (650, 450), (500, 350)]
        for pos in city_positions:
            pygame.draw.circle(screen, green, pos, 60)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
