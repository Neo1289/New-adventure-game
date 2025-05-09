from game_settings import pygame

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


class InventorySprite(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((139,69,19))  # Fill with brown color
        self.rect = self.image.get_rect(center=(width + 100, height + 100))





