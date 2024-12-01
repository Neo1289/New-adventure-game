from game_settings import *

frames = []
bat_folder = path.join('resources', 'bat')
for file_name in listdir(bat_folder):
    full_path = path.join(bat_folder, file_name)
    surf = pygame.image.load(full_path).convert_alpha()
    frames.append(surf)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(groups)

        self.frames, self.frames_index = frames,0
        self.image = self.frames[self.frames_index]
        self.animation_speed = 15

        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.Vector2()
        self.speed = 300

    def animate(self, dt):
        self.frames_index += self.animation_speed * dt
        self.image = self.frames[int(self.frames_index) % len(self.frames)]

    def update(self, dt):
        self.animate(dt)


