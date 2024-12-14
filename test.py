import pygame
import sys
from test_two import *

# Initialize Pygame
pygame.init()

# Set up display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Game")

# Set up clock
clock = pygame.time.Clock()

def main_game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Example: Press 'M' to start the minigame
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    # Call the minigame and wait until it finishes
                    run_minigame(screen)

        # Main game logic and rendering
        screen.fill((50, 150, 50))  # Fill the screen with a green color

        # Example main game text
        font = pygame.font.Font(None, 36)
        text = font.render("Main Game: Press 'M' for Minigame", True, (255, 255, 255))
        screen.blit(text, (200, SCREEN_HEIGHT // 2))

        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_game_loop()
