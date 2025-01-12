from game_settings import (display_surface,
                           pygame,
                           maps,
                           TILE_SIZE,
                           FONT_SIZE,
                           WINDOW_WIDTH,WINDOW_HEIGHT,
                           button_color,
                           sys)
from sprites import GroundSprite,CollisionSprite,AreaSprite

class ToolBar():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        dt = self.clock.tick() / 10000

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False

            display_surface.fill((0, 0, 0))
            pygame.display.update()

        return
