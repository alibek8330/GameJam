from libraries import *
class Wave:
    def __init__(self, x, y, width, height, speed, color='blue'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = pygame.Color(color)
        self.alive = True

    def move(self):
        self.x += self.speed
        self.height *= 0.99
        
        if self.height < 5:
            self.alive = False

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.width, self.height))

    def change_color(self, new_color):
        self.color = pygame.Color(new_color)

