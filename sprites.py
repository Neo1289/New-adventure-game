from game_settings import pygame, wall

class GroundSprite(pygame.sprite.Sprite):
    def __init__(self, pos ,surf, groups):
         super().__init__(groups)
         self.image = surf
         self.rect = self.image.get_rect(topleft = pos)
         self.ground = True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, name):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.name = name
        self.resources = 1

class AreaSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width,height,groups):
        super().__init__(groups)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, width, height)

class BonusSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, name,delay):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.name = name
        self.resources = 1
        self.spawn_time = pygame.time.get_ticks()
        self.delay = delay

    def update(self,dt):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_time >= self.delay:
            self.kill()


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y,groups):
        super().__init__(groups)
        self.image = wall
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed_x = 2000
        self.dangerous = True

    def update(self, dt):
        self.rect.centerx +=  self.speed_x * dt
        if self.rect.centery > 3000:
            self.kill()

class ColumnSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, name):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.name = name
        self.resources = 1

    def update(self, dt):
        if self.resources == 0:
            self.kill()








