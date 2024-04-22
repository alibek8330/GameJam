import pygame
from assets import home_img, flow_frames

class Home(pygame.sprite.Sprite):
    def __init__(self, pos, hp):
        super().__init__()
        self.image = home_img
        self.rect = self.image.get_rect(center=pos)
        self.hp = hp

class Flow(pygame.sprite.Sprite):
    def __init__(self, pos, frame_index):
        super().__init__()
        self.image = flow_frames[0]  # Initialize with the first frame
        self.rect = self.image.get_rect(center=pos)  # Initialize rect with position
        self.update_frame(frame_index)

    def move(self, frame_index):
        self.update_frame(frame_index)

    def update_frame(self, frame_index):
        # Safely update frame_index to avoid out-of-range errors
        frame_index = frame_index % len(flow_frames)
        self.image = flow_frames[frame_index]
        # Update rect to maintain the current position with the new image dimensions
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)
