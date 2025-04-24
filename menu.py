import pygame
import sys

class GameMenu:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        # Define colors as class attributes
        self.WHITE = (255, 255, 255)
        self.bg_color = (0, 0, 0)
        self.game_duration = 60000  # 60 seconds in milliseconds

        # Get display surface from pygame directly
        self.display_surface = pygame.display.get_surface()
        self.screen_width = self.display_surface.get_width()
        self.screen_height = self.display_surface.get_height()
        self.start_time = pygame.time.get_ticks()
        self.timer_font = pygame.font.SysFont('Arial', 36)

    def display_timer(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        self.remaining_time = max(0, (self.game_duration - elapsed_time) // 1000)
        timer_text = self.timer_font.render(f"Time: {self.remaining_time}", True, self.WHITE)
        timer_rect = timer_text.get_rect(midtop=(self.screen_width // 2, 20))
        self.display_surface.blit(timer_text, timer_rect)

    def display_instructions(self):
        font = pygame.font.SysFont('Arial', 18)
        instructions = [
            "Use Arrow Keys to move, SPACE to jump, ESC to exit",
            "get more than 30 coins for a free potion"
        ]
        for i, line in enumerate(instructions):
            text = font.render(line, True, self.WHITE)
            self.display_surface.blit(text, (20, 20 + i * 25))

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
            self.display_timer()
            pygame.display.update()

        return