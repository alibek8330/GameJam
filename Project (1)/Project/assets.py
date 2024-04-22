import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def load_scaled_image(path, width, height):
    image = pygame.image.load(f"SaveCities\\img\\{path}")
    return pygame.transform.scale(image, (width, height))

bg_frames = [load_scaled_image(f"frame{i}.png", SCREEN_WIDTH + 200, SCREEN_HEIGHT + 200) for i in range(1, 5)]

flow_frames = [load_scaled_image(f"flow{i}.png", 200, 200) for i in range(1, 4)]

home_img = load_scaled_image("home_img.png", 250, 250)
coin_icon = load_scaled_image("coin.png", 32, 32)
bags_icon = load_scaled_image("bags.png", 80, 80)
vacuum_icon = load_scaled_image("vacuum.png", 80, 80)
damb_icon = load_scaled_image("damb1.png", 80, 80)
player_image = load_scaled_image("player.png", 200, 200)

flow1 = load_scaled_image("flow1.png", 200, 200)
flow2 = load_scaled_image("flow2.png", 200, 200)
flow3 = load_scaled_image("flow3.png", 200, 200)
flow4 = load_scaled_image("flow4.png", 200, 200)
flow5 = load_scaled_image("flow5.png", 200, 200)
flow6 = load_scaled_image("flow6.png", 200, 200)
flow7 = load_scaled_image("flow7.png", 200, 200)
flow8 = load_scaled_image("flow8.png", 200, 200)
flow9 = load_scaled_image("flow9.png", 200, 200)