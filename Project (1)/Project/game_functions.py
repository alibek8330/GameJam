import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, RED, WHITE
from assets import bg_frames, coin_icon, home_img, bags_icon, vacuum_icon, damb_icon, flow_frames, player_image
from random import choice
from assets import flow1, flow2, flow3, flow4, flow5, flow6, flow7, flow8, flow9

def game(screen, gui):
    global frame_index, money, bags_pos, vacuum_pos, damb_pos, tool_dragging, HP
    frame_index = 0
    money = 0
    bags_pos = [20, SCREEN_HEIGHT - 80]
    vacuum_pos = [120, SCREEN_HEIGHT - 80]
    damb_pos = [220, SCREEN_HEIGHT - 80]
    tool_dragging = None
    HP = 100
    running = True
    last_update_time = pygame.time.get_ticks()
    flow_animation_interval = 1000
    clock = pygame.time.Clock()

    instruction_icon = pygame.transform.scale(player_image, (200, 200))

    added_days = []
    flood_days = []
    last_flood_direction = None
    flood_positions = {
        'south': (900, 120),
        'north': (900, SCREEN_HEIGHT - 200),
        'east': (1400, 500),
        'west': (400, 500),
        'northeast': (1200, 250),
        'northwest': (600, 250),
        'southeast': (1200, 800),
        'southwest': (600, 800)
    }
    flood_directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest']
    flow_frames = [flow1, flow2, flow3, flow4, flow5, flow6, flow7, flow8, flow9]
    tool_costs = {'bags': -100, 'vacuum': -150, 'damb': -150}

    bags_start_pos = bags_pos[:]
    vacuum_start_pos = vacuum_pos[:]
    damb_start_pos = damb_pos[:]

    while running:
        screen.fill(BLACK)
        screen.blit(bg_frames[frame_index], (-50, -100))
        screen.blit(home_img, (SCREEN_WIDTH / 2 - 125, SCREEN_HEIGHT / 2 - 125))
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(bags_pos[0], bags_pos[1], bags_icon.get_width(), bags_icon.get_height()).collidepoint(event.pos):
                    tool_dragging = 'bags'
                elif pygame.Rect(vacuum_pos[0], vacuum_pos[1], vacuum_icon.get_width(), vacuum_icon.get_height()).collidepoint(event.pos):
                    tool_dragging = 'vacuum'
                elif pygame.Rect(damb_pos[0], damb_pos[1], damb_icon.get_width(), damb_icon.get_height()).collidepoint(event.pos):
                    tool_dragging = 'damb'
            elif event.type == pygame.MOUSEBUTTONUP:
                if tool_dragging:
                    new_pos = [event.pos[0], event.pos[1]]
                    flood_position = flood_positions[last_flood_direction]  # Corrected variable name usage
                    if pygame.Rect(flood_position[0], flood_position[1], 100, 100).collidepoint(new_pos):
                        if money + tool_costs[tool_dragging] >= 0:
                            money += tool_costs[tool_dragging]
                            flow_frame_index = 0  # Reset flood due to tool application
                            print(f"{tool_dragging.capitalize()} used, flood reset!")
                        else:
                            print("Not enough money to use this tool!")
                    exec(f"{tool_dragging}_pos = {tool_dragging}_start_pos[:]")  # Reset tool position
                    tool_dragging = None
            elif event.type == pygame.MOUSEMOTION and tool_dragging:
                exec(f"{tool_dragging}_pos[0], {tool_dragging}_pos[1] = event.pos")

        screen.blit(bags_icon, bags_pos)
        screen.blit(vacuum_icon, vacuum_pos)
        screen.blit(damb_icon, damb_pos)

        seconds = current_time / 1000
        days = int(seconds // 2)

        if days % 30 == 0 and days not in added_days:
            money += 400
            added_days.append(days)

        if days % 10 == 0 and days not in flood_days:
            flood_direction = choice(flood_directions)
            last_flood_direction = flood_direction
            flood_position = flood_positions[flood_direction]
            flood_days.append(days)
            flow_frame_index = 0  # Reset to smallest flow at the start of each flood period

        if current_time - last_update_time > flow_animation_interval:
            if flow_frame_index < len(flow_frames) - 1:
                flow_frame_index += 1  # Increase flow size every second
            last_update_time = current_time

        days_text = gui.font.render(f"Day: {days}", True, BLACK)
        money_text = gui.font.render(f"Money: ${money}", True, BLACK)
        screen.blit(days_text, (SCREEN_WIDTH - days_text.get_width() - 10, 10))
        screen.blit(coin_icon, (SCREEN_WIDTH - days_text.get_width() - 110, 10))
        screen.blit(money_text, (SCREEN_WIDTH - days_text.get_width() - money_text.get_width() - 20, 10))
        screen.blit(flow_frames[flow_frame_index], flood_position)

        screen.blit(instruction_icon, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200))

        font = pygame.font.SysFont(None, 30)
        text_surface = font.render("Player", True, WHITE)
        text_rect = text_surface.get_rect(center=(instruction_icon.get_width() // 2, 180))
        instruction_icon.blit(text_surface, text_rect.topleft)
        
        hp_text = font.render(f"{HP}hp", True, RED)
        hp_rect = text_surface.get_rect(center=(home_img.get_width() // 2 - 40, 150))
        home_img.blit(hp_text, hp_rect.topleft)

        clock.tick(60)
        pygame.display.update()


def instruction(screen, gui):
    running = True
    clock = pygame.time.Clock()
    button_back = (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT - 100, 200, 50)

    while running:
        screen.fill(BLACK)
        screen.blit(bg_frames[0], (0, -200))

        gui.draw_text("Fight the Flood - Instructions", "black", 200, 30+100)
        gui.draw_text("Objective:", "black", 220, 80+100)
        gui.draw_text("Survive the floods and save the city.", "white", 250, 110+110)
        gui.draw_text("Components:", "black", 220, 160+100)
        gui.draw_text("Timer, Money, Tools, City, Health, Progress, River.", "white", 250, 190+110)
        gui.draw_text("Setup:", "black", 220, 240+100)
        gui.draw_text("Start with 400 coins. Place instruments wisely.", "white", 250, 270+110)
        gui.draw_text("Rules of Play:", "black", 220, 320+100)
        gui.draw_text("1. Build up defenses before attacks start.", "white", 250, 350+110)
        gui.draw_text("2. Three rounds of increasing difficulty.", "white", 250, 380+120)
        gui.draw_text("3. Manage resources and build anytime.", "white", 250, 410+130)
        gui.draw_text("FAQ:", "black", 220, 460+120)
        gui.draw_text("Yes, we're musketeers :)", "white", 250, 490+130)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gui.is_button_clicked(button_back):
                    print("Button clicked back")
                    return

        gui.draw_button("Back", "black", button_back, "green")

        pygame.display.update()
        clock.tick(60)



def main_menu(screen, gui):
    click = False
    frame_index = 0
    clock = pygame.time.Clock()
    while True:
        screen.fill(BLACK)  # Clear screen
        screen.blit(bg_frames[frame_index % len(bg_frames)], (-50, -100))

        # Define buttons
        button_start = (SCREEN_WIDTH/2 - 100, 200, 200, 50)
        button_instructions = (SCREEN_WIDTH / 2 - 120, 350, 250, 50)
        button_quit = (SCREEN_WIDTH / 2 - 100, 500, 200, 50)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                mx, my = event.pos
                if gui.is_button_clicked(button_start) and click:
                    print("GAME")
                    game(screen, gui)
                if gui.is_button_clicked(button_instructions) and click:
                    print("Instructions")
                    instruction(screen, gui)
                if gui.is_button_clicked(button_quit) and click:
                    pygame.quit()
                    sys.exit()

        # Update UI
        gui.draw_button("Start", "black", button_start, "green" if gui.is_button_clicked(button_start) else None)
        gui.draw_button("Instructions", "black", button_instructions, "green" if gui.is_button_clicked(button_instructions) else None)
        gui.draw_button("Quit", "black", button_quit, "green" if gui.is_button_clicked(button_quit) else None)

        # Update frame
        pygame.display.update()
        clock.tick(10)
