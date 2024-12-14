from game_settings import pygame

class GroundSprite(pygame.sprite.Sprite):
    def __init__(self, pos ,surf, groups):
         super().__init__(groups)
         self.image = surf
         self.rect = self.image.get_rect(topleft = pos)
         self.ground = True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

class AreaSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width,height,groups):
        super().__init__(groups)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, width, height)





