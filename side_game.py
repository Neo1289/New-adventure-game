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


class SideGame():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = PlayerSide()
        self.display_surface = display_surface

    def run(self):
        dt = self.clock.tick(60)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False


            self.display_surface.fill((0, 0, 0))
            self.player.update(dt)
            self.display_surface.blit(self.player.image, (WINDOW_HEIGHT / 2, WINDOW_WIDTH / 2))
            pygame.display.update()

        return
