import random
from game_settings import frames, pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,frames,groups):
        super().__init__(groups)

        self.frames, self.frames_index = frames,0
        self.image = self.frames[self.frames_index]
        self.animation_speed = 15

        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.Vector2(pos)
        self.list = [-1,1]
        self.direction = pygame.Vector2(random.choice(self.list), random.choice(self.list))
        self.speed = 100
        self.sprite_type = True

    def animate(self, dt):
        self.frames_index += self.animation_speed * dt
        self.image = self.frames[int(self.frames_index) % len(self.frames)]

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def update(self, dt):
        self.animate(dt)
        self.move(dt)
        if self.rect.center > (3000,3000) or self.rect.center < (-3000,-3000) :
            self.kill()



