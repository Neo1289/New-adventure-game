
import sys
from flame import Flame
from game_settings import pygame, player_flame_frames
from groups import allSprites

class StoryTeller:
    def __init__(self, location):
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
        self.flame = Flame((self.screen_width//2, self.screen_height//2), player_flame_frames, self.allsprites)
        self.location = location

    def display_instructions(self):
        font = pygame.font.SysFont('Georgia', 20)
        instructions = [

            f"{self.location} \n\n"
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
            elapsed_time = pygame.time.get_ticks() - self.start_time
            if elapsed_time >= 10000:
                self.running = False

            self.display_surface.fill(self.bg_color)
            self.display_instructions()
            self.allsprites.draw(self.flame.rect.center)
            self.allsprites.update(dt)

            pygame.display.update()

        return