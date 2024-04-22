import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from gui import GUI
from game_functions import main_menu, game

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Save Cities")
    gui = GUI(screen)
    main_menu(screen, gui)
    # game(screen, gui)

if __name__ == "__main__":
    main()
