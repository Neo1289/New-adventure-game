from game_settings import (display_surface,
                           pygame,
                           maps,
                           TILE_SIZE,
                           FONT_SIZE,
                           WINDOW_WIDTH,WINDOW_HEIGHT,
                           button_color,
                           sys,
                           join
                           )
from player_side_game import PlayerSide
from groups import allSprites

class SideGame():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.all_sprites = allSprites()
        self.player = PlayerSide(self.all_sprites)

    def run(self):
        dt = self.clock.tick(60)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False


            display_surface.fill((0, 0, 0))
            self.all_sprites.draw(self.player.rect.center)
            self.all_sprites.update(dt)
            pygame.display.update()

        return
