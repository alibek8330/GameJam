import pygame
from settings import BLACK, WHITE, GREEN, BLUE, RED

class GUI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 55)
        self.colors = {
            "blue": BLUE,
            "white": WHITE,
            "black": BLACK,
            "green": GREEN,
            "red": RED
        }

    def draw_text(self, text, color, x, y):
        text_surface = self.font.render(text, True, self.colors[color])
        self.screen.blit(text_surface, (x, y))

    def draw_button(self, text, color, rect, hover_color=None):
        mx, my = pygame.mouse.get_pos()
        rect_obj = pygame.Rect(rect)
        if rect_obj.collidepoint((mx, my)):
            pygame.draw.rect(self.screen, self.colors[hover_color if hover_color else color], rect_obj)
        else:
            pygame.draw.rect(self.screen, self.colors[color], rect_obj)
        text_x = rect[0] + (rect[2] - self.font.size(text)[0]) / 2
        text_y = rect[1] + (rect[3] - self.font.size(text)[1]) / 2
        self.draw_text(text, "white", text_x, text_y)

    def is_button_clicked(self, rect):
        mx, my = pygame.mouse.get_pos()
        return pygame.Rect(rect).collidepoint((mx, my))
