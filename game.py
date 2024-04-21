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
green = (65, 173, 38)

frame1 = pygame.image.load(r"SaveCities\\img\\frame1.png")
frame1 = pygame.transform.scale(frame1, (screen_width + 200, screen_height + 200))
frame2 = pygame.image.load(r"SaveCities\\img\\frame2.png")
frame2 = pygame.transform.scale(frame2, (screen_width + 200, screen_height + 200))
frame3 = pygame.image.load(r"SaveCities\\img\\frame3.png")
frame3 = pygame.transform.scale(frame3, (screen_width + 200, screen_height + 200))
frame4 = pygame.image.load(r"SaveCities\\img\\frame4.png")
frame4 = pygame.transform.scale(frame4, (screen_width + 200, screen_height + 200))

bg_frames = [frame1, frame2, frame3, frame4]
frame_index = 0
clock = pygame.time.Clock()


flow1 = pygame.image.load(r"SaveCities\\img\\flow1.png")
flow1 = pygame.transform.scale(flow1, (100, 100))
flow2 = pygame.image.load(r"SaveCities\\img\\flow2.png")
flow2 = pygame.transform.scale(flow2, (100, 100))
flow3 = pygame.image.load(r"SaveCities\\img\\flow3.png")
flow3 = pygame.transform.scale(flow3, (100, 100))
# flow4 = pygame.image.load(r"SaveCities\\img\\flow4.png")
# flow4 = pygame.transform.scale(flow4, (100, 100))
# flow5 = pygame.image.load(r"SaveCities\\img\\flow5.png")
# flow5 = pygame.transform.scale(flow5, (100, 100))
flow_frames = [flow1, flow2, flow3]
flow_frame_index = 0
# clock = pygame.time.Clock()

def main_menu():
    click = False
    global frame_index
    while True:
        screen.blit(bg_frames[frame_index], (-50, -100))
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
        frame_index = (frame_index + 1) % len(bg_frames)
        clock.tick(5)
        pygame.display.update()


class GUI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 55)
        self.colors = {
            "blue": pygame.Color(0, 0, 255),
            "white": pygame.Color(255, 255, 255),
            "black": pygame.Color(0, 0, 0),
            "green": pygame.Color(65, 173, 38),
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


def load_img(path):
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (150, 150))
    return image


home_img = load_img(r"SaveCities\\img\\home_img.png")
home_img = pygame.transform.scale(home_img, (250, 250))

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


tool1_start_pos = [20, screen_height - 80]
tool2_start_pos = [120, screen_height - 80]
tool1_pos = tool1_start_pos[:]
tool2_pos = tool2_start_pos[:]
tool_dragging = None 

DAMAGE = 10
MAXHP = 100
HP = 100
RATIO = HP / MAXHP


class Home(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = home_img
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width / 2, screen_height / 2)
        self.hp = HP

class Flow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = flow_frames[flow_frame_index]
        self.rect = self.image.get_rect()
    
    def move(self):
        flow_frame_index = (flow_frame_index + 1) % len(flow_frames)
        self.image = flow_frames[flow_frame_index]


class HpBarHome():
    def __init__(self, x, y, width, height, hp, MAXHP):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hp = hp
        self.MAXHP = MAXHP

    def draw(self, screen):
        RATIO = self.hp / self.MAXHP
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width * RATIO, self.height))

HP_bar = HpBarHome(685, 500, 200, 20, HP, MAXHP)


def game():
    global screen
    global frame_index
    global flow_frame_index
    global money
    global tool1_pos
    global tool2_pos
    global tool_dragging
    global HP
    running = True
    last_update_time = pygame.time.get_ticks()
    flow_animation_interval = 10000
    while running:
        screen.blit(bg_frames[frame_index], (-50, -100))
        HP_bar.draw(screen)
        screen.blit(home_img, (screen_width / 2 - 65, screen_height / 2 - 65))
        current_time = pygame.time.get_ticks()

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
                    tool1_pos = tool1_start_pos[:]
                elif tool_dragging == "tool2":
                    tool2_pos = tool2_start_pos[:]
                tool_dragging = None
            elif event.type == pygame.MOUSEMOTION and tool_dragging:
                if tool_dragging == "tool1":
                    tool1_pos[0], tool1_pos[1] = event.pos
                elif tool_dragging == "tool2":
                    tool2_pos[0], tool2_pos[1] = event.pos
        platform1 = pygame.draw.rect(screen, green, (0, 780, 500, 300), 500)
        platform2 = pygame.draw.rect(screen, green, (1350, 0, 500, 50), 500)
        screen.blit(tool1_icon, tool1_pos)
        screen.blit(tool2_icon, tool2_pos)
        seconds = (
            pygame.time.get_ticks() - start_ticks
        ) / 1000  # Преобразование миллисекунд в секунды
        days = int(seconds // 10)  # Каждые 10 секунды соответствуют одному дню

        if (flow_frame_index == 2):
            HP -= 10
        if (
            seconds % 30 == 0 and seconds != 0 and seconds >= 30
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
        frame_index = (frame_index + 1) % len(bg_frames)
        if current_time - last_update_time > flow_animation_interval:
            # Update the flow animation
            screen.blit(flow_frames[flow_frame_index], (700, 350))
            flow_frame_index = (flow_frame_index + 1) % len(flow_frames)
            # Reset the last update time
            last_update_time = current_time
        clock.tick(5)
        pygame.display.update()
        pygame.time.delay(10)


if __name__ == "__main__":
    main_menu()
