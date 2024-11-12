from game_settings import *

class SideGame():
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            display_surface.fill((0, 0, 0))

            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    side_game = SideGame()
    side_game.run()
