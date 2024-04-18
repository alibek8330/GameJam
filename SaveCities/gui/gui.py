from libraries import *

pygame.init()
pygame.font.init()

class GUI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 55)
        self.colors = {
            "blue": pygame.Color(0, 0, 255),
            "white": pygame.Color(255, 255, 255),
            "black": pygame.Color(0, 0, 0),
            "green": pygame.Color(0, 255, 0),
        }

    def draw_text(self, text, color, x, y):
        text_surface = self.font.render(text, True, self.colors[color])
        text_rect = text_surface.get_rect(topleft=(x, y))
        self.screen.blit(text_surface, text_rect)

    def draw_button(self, text, color, rect, hover_color=None):
        rect_obj = pygame.Rect(rect)
        mx, my = pygame.mouse.get_pos()

        if rect_obj.collidepoint((mx, my)) and hover_color is not None:
            pygame.draw.rect(self.screen, self.colors[hover_color], rect_obj)
        else:
            pygame.draw.rect(self.screen, self.colors[color], rect_obj)
        
        text_x = rect[0] + (rect[2] / 2) - (self.font.size(text)[0] / 2)
        text_y = rect[1] + (rect[3] / 2) - (self.font.size(text)[1] / 2)
        self.draw_text(text, "white", text_x, text_y)

    def is_button_clicked(self, rect):
        rect_obj = pygame.Rect(rect)
        mx, my = pygame.mouse.get_pos()
        return rect_obj.collidepoint((mx, my))