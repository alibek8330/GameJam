from libraries import *
from gui.colors import *
from gui.gui import GUI

screen_width, screen_height = 1000, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Save Cities")
gui = GUI(screen)

def main_menu():
    click = False
    while True:
        screen.fill(gui.colors["white"])
        gui.draw_text("Save Cities", "black", 280, 20)

        button_start = (300, 100, 200, 50)
        button_instructions = (300, 200, 200, 50)
        button_quit = (300, 300, 200, 50)

        if gui.is_button_clicked(button_start) and click:
            game()  # Игра начнется здесь
        if gui.is_button_clicked(button_instructions) and click:
            instructions()  # Отобразить инструкции
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