import pygame
import sys
import random
from PIL import Image, ImageSequence

pygame.init()
pygame.font.init()

infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h
screen = pygame.display.set_mode(
    (infoObject.current_w, infoObject.current_h), pygame.RESIZABLE
)

fullscreen = True

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

bg_game = pygame.image.load(r"SaveCities\\img\\bg_game.jpg")
bg_game = pygame.transform.scale(bg_game, (screen_width, screen_height))

frame1 = pygame.image.load(r"SaveCities\\img\\left_image.png")
frame1 = pygame.transform.scale(frame1, (screen_width + 155, screen_height + 100))
frame2 = pygame.image.load(r"SaveCities\\img\\middle_image.png")
frame2 = pygame.transform.scale(frame2, (screen_width + 155, screen_height + 100))
frame3 = pygame.image.load(r"SaveCities\\img\\right_image.png")
frame3 = pygame.transform.scale(frame3, (screen_width + 155, screen_height + 100))

frames = [frame1, frame2, frame3]
frame_index = 0
clock = pygame.time.Clock()

def main_menu():
    click = False
    global frame_index
    screen.blit(bg_game, (0, 0))
    while True:
        screen.blit(frames[frame_index], (-100, -30))
        frame_index = (frame_index + 1) % len(frames)
        clock.tick(10)
        gui.draw_text("Save Cities", "black", screen_width / 2 - 105 , 50)

        button_start = (screen_width/2 - 100, 200, 200, 50)
        button_instructions = (screen_width / 2 - 120, 350, 250, 50)
        button_quit = (screen_width / 2 - 100, 500, 200, 50)

        if gui.is_button_clicked(button_start) and click:
            game()

        if gui.is_button_clicked(button_instructions) and click:
            instructions()

        if gui.is_button_clicked(button_quit) and click:
            pygame.quit()
            sys.exit()

        gui.draw_button("Start", "black", button_start, "green")
        gui.draw_button("Instructions", "black", button_instructions, "green")
        gui.draw_button("Quit", "black", button_quit, "green")

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


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


pygame.display.set_caption("Save Cities")
gui = GUI(screen)


def load_city_image(path):
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (150, 150))
    return image

def center_content(screen_width, screen_height):
    city_positions = [
        (screen_width / 2 - 300, screen_height / 2 - 100),
        (screen_width / 2 + 300, screen_height / 2 - 100),
        (screen_width / 2 - 300, screen_height / 2 + 100),
        (screen_width / 2 + 300, screen_height / 2 + 100)
    ]
    astana_position = (screen_width / 2, screen_height / 2)
    tokayev_position = (screen_width / 2, screen_height / 2 - 100)

    return city_positions, astana_position, tokayev_position

city_image = load_city_image(r"SaveCities\\img\\city.jpg")
city_image = pygame.transform.scale(city_image, (100, 100))
astana_image = load_city_image(r"SaveCities\\img\\astana.jpg")
astana_image = pygame.transform.scale(astana_image, (100, 100))
tokayev_image = load_city_image(r"SaveCities\\img\\tokayev.png")
tokayev_image = pygame.transform.scale(tokayev_image, (80, 100))


# Шрифт для отображения дней
font = pygame.font.Font(None, 36)

# Часы для отслеживания времени
clock = pygame.time.Clock()

# Время начала игры
start_ticks = pygame.time.get_ticks()
money = 400
# Загрузка изображения монеты
coin_icon = pygame.image.load(r"SaveCities\\img\\coin.png")
coin_icon = pygame.transform.scale(coin_icon, (32, 32))
# Tools
tool1_icon = pygame.image.load(r"SaveCities\\img\\bags.png")
tool1_icon = pygame.transform.scale(tool1_icon, (80, 80)) 
tool2_icon = pygame.image.load(r"SaveCities\\img\\vacuum.png")
tool2_icon = pygame.transform.scale(tool2_icon, (80, 80))

# Исходные позиции иконок инструментов
tool1_start_pos = [20, screen_height - 80]
tool2_start_pos = [120, screen_height - 80]
tool1_pos = tool1_start_pos[:]
tool2_pos = tool2_start_pos[:]
tool_dragging = None  # Никакой инструмент не перетаскивается


def game():
    global screen
    global frame_index
    global money
    global tool1_pos
    global tool2_pos
    global tool_dragging
    running = True
    city_positions = center_content(screen_width, screen_height)[0]
    astana_position = center_content(screen_width, screen_height)[1]
    tokayev_position = center_content(screen_width, screen_height)[2]
    while running:
        screen.blit(bg_game, (0, 0))
        for city in city_positions:
            screen.blit(city_image, city_image.get_rect(center=city))
        screen.blit(tokayev_image, tokayev_image.get_rect(center=tokayev_position))
        screen.blit(astana_image, astana_image.get_rect(center=astana_position))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if tool1_icon.get_rect(topleft=tool1_pos).collidepoint(event.pos):
                    tool_dragging = "tool1"
                elif tool2_icon.get_rect(topleft=tool2_pos).collidepoint(event.pos):
                    tool_dragging = "tool2"
            elif event.type == pygame.MOUSEBUTTONUP:
                if tool_dragging == "tool1":
                    tool1_pos = tool1_start_pos[:]  # Возвращение на исходную позицию
                elif tool_dragging == "tool2":
                    tool2_pos = tool2_start_pos[:]
                tool_dragging = None
            elif event.type == pygame.MOUSEMOTION and tool_dragging:
                if tool_dragging == "tool1":
                    tool1_pos[0], tool1_pos[1] = event.pos
                elif tool_dragging == "tool2":
                    tool2_pos[0], tool2_pos[1] = event.pos

        screen.blit(frames[frame_index], (-100, -30))
        frame_index = (frame_index + 1) % len(frames)
        platform1 = pygame.draw.rect(screen, white, (0, 780, 500, 300), 500)
        platform1 = pygame.draw.rect(screen, white, (1350, 0, 500, 50), 500)
        screen.blit(tool1_icon, tool1_pos)
        screen.blit(tool2_icon, tool2_pos)
        seconds = (
            pygame.time.get_ticks() - start_ticks
        ) / 1000  # Преобразование миллисекунд в секунды
        days = int(seconds // 4)  # Каждые 4 секунды соответствуют одному дню

        if (
            seconds % 30 == 0 and seconds != 0
        ):  # Проверка, чтобы не увеличить деньги сразу при старте
            money += 400
        days_text = font.render(f"Day: {days}", True, black)
        money_text = font.render(f"{money}", True, black)
        screen.blit(
            days_text, (screen_width - days_text.get_width() - 10, 10)
        )  # Позиционирование в правом верхнем углу
        screen.blit(
            coin_icon, (screen_width - days_text.get_width() - 110, 10)
        )  # Позиционирование иконки монеты
        screen.blit(
            money_text,
            (screen_width - days_text.get_width() - money_text.get_width() - 20, 10),
        )
        clock.tick(60)

        pygame.display.update()
        pygame.time.delay(60)


if __name__ == "__main__":
    main_menu()
