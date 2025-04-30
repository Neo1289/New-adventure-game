
import sys
from flame import Flame
from game_settings import pygame, flame_frames
from groups import allSprites

class GameMenu:
    def __init__(self, objects):
        self.running = True
        self.clock = pygame.time.Clock()
        # Define colors as class attributes
        self.WHITE = (255, 255, 2)
        self.bg_color = (0, 30, 20)

        # Get display surface from pygame directly
        self.display_surface = pygame.display.get_surface()
        self.screen_width = self.display_surface.get_width()
        self.screen_height = self.display_surface.get_height()
        self.start_time = pygame.time.get_ticks()
        self.timer_font = pygame.font.SysFont('Georgia', 30)
        self.allsprites = allSprites()
        self.flame = Flame((self.screen_width//2, self.screen_height//2), flame_frames, self.allsprites)
        self.objects = objects

    def display_instructions(self):
        font = pygame.font.SysFont('Georgia', 20)
        instructions = [
            "Coin collection game: \n\n"
            "Use Arrow Keys to move, SPACE to jump, ESC to exit \n"
            "get more than 30 coins for a free potion \n\n"
            "Main game: \n\n"
            "Use arrows to move the character around \n"
            "Y to enter areas or inspect objects \n"
            "Press 1 to use the potion \n"
            "Press m to access the menu \n"
            "Press f to release the runic fire \n"
            "Press space to cast a rune \n\n"
            "Inventory: \n\n"
            f"{self.objects} \n\n"
            "Press ESC to return to the game \n"
        ]
        for i, line in enumerate(instructions):
            text = font.render(line, True, self.WHITE)
            self.display_surface.blit(text, (30, 30 + i * 35))


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

            self.display_surface.fill(self.bg_color)
            self.display_instructions()
            self.allsprites.draw(self.flame.rect.center)
            self.allsprites.update(dt)

            pygame.display.update()

        return