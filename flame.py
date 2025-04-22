
from game_settings import pygame, randint


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


class PlayerFlame(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(groups)
        self.frames = frames
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.spawn_time = pygame.time.get_ticks()
        self.groups = groups


    def animate(self, dt):

        self.frames_index += 7 * dt
        self.image = self.frames[int(self.frames_index) % len(self.frames)]

    def flame(self, dt):
        self.animate(dt)
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time >= 300:
            self.pos = pygame.Vector2(randint(-20, 20), randint(-20, 20)) + self.pos
            PlayerFlame(self.pos, self.frames, self.groups)
            self.kill()
        if current_time - self.spawn_time >=3000:
            self.kill()

    def update(self, dt):
        self.flame(dt)



