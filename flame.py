
from game_settings import pygame

class Flame(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(groups)
        self.frames = frames
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.dangerous = True

    def animate(self, dt):

        self.frames_index += 7 * dt
        self.image = self.frames[int(self.frames_index) % len(self.frames)]

    def update(self, dt):
        self.animate(dt)
