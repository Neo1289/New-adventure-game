from game_settings import (display_surface,
                           pygame,
                           sys,
                            join
                           )
from player import Player

class Platform(Player):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(pos, groups, collision_sprites)

    def input(self):
        super().input()
        self.direction.y = 0

class SideGame():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.display_surface = display_surface
        self.platform_group = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.platform_player = Platform((100, 500), self.platform_group, self.collision_sprites)
        self.ground_rect = pygame.Rect(0, 500, self.display_surface.get_width(), 50)

    def run(self):

        while self.running:
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False

            # Clear screen and draw
            self.display_surface.fill((0, 0, 0))
            # Draw ground
            pygame.draw.rect(self.display_surface, (100, 50, 0), self.ground_rect)
            self.platform_group.update(dt)
            self.platform_group.draw(self.display_surface)

            pygame.display.update()

        return
