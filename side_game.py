from game_settings import (display_surface,
                           pygame,
                           sys,
                            join
                           )
from player import Player

class Platform(Player):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(pos, groups, collision_sprites)
        self.jump_strength = 30
        self.on_air = False
        self.gravity = 1
        self.jumping = False

    def input(self):
        super().input()
        if self.keys[pygame.K_SPACE]:
            self.jumping = True
            self.on_air = True
            self.jump()

    def jump(self):
        if self.on_air and self.jumping:
            self.direction.y = -self.jump_strength
            self.jumping = False

    def handle_gravity(self):
        if self.on_air:
            self.direction.y += self.gravity
            if self.rect.bottom >= 500:
                self.direction.y = 0
                self.rect.bottom = 500
                self.on_air = False

    def update(self, dt):
        super().update(dt)
        self.handle_gravity()

class SideGame():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.display_surface = display_surface
        self.platform_group = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.platform_player = Platform((100, 510), self.platform_group, self.collision_sprites)
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

            # Clear screen and draw
            self.display_surface.fill((0, 0, 0))
            # Draw ground
            pygame.draw.rect(self.display_surface, (100, 50, 0), self.ground_rect)
            # Draw the platform player
            self.platform_group.draw(self.display_surface)
            self.platform_group.update(dt)

            pygame.display.update()

        return
