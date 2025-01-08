from game_settings import (display_surface,
                           pygame,
                           maps,
                           TILE_SIZE,
                           FONT_SIZE,
                           WINDOW_WIDTH,WINDOW_HEIGHT,
                           button_color,
                           sys)
from sprites import GroundSprite,CollisionSprite,AreaSprite
from player import Player
from groups import allSprites
from enemy import Enemy,frames

class SideGame():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.all_sprites = allSprites()
        self.collision_sprites = pygame.sprite.Group()

    def run(self):
        dt = self.clock.tick() / 10000

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    pass

            display_surface.fill((0, 0, 0))
            self.all_sprites.update(dt)
            pygame.display.update()

        pygame.quit()
        sys.exit()
