from libraries import *

def game(screen, screen_width, screen_height):
    running = True
    waves = [] 
    while running:
        screen.fill(white)

        pygame.draw.ellipse(screen, blue, pygame.Rect(25, 25, 950, 600), width=50)

        city_positions = [(250, 250), (650, 150), (250, 400), (650, 450), (500, 350)]
        for pos in city_positions:
            pygame.draw.circle(screen, green, pos, 60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if random.randint(1, 60) == 1: 
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            width = random.randint(50, 100)
            height = random.randint(20, 50)
            speed = random.randint(-2, 2)
            waves.append(Wave(x, y, width, height, speed))

        for wave in waves:
            wave.move()
            wave.draw(screen)

        waves = [wave for wave in waves if 0 < wave.x + wave.width < screen_width]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        pygame.display.update()