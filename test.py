from enemy import *


import pygame
import sys

# Initialize Pygame
pygame.init()

# ---------------------------
# Configuration Parameters
# ---------------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Pygame Black Window"
FPS = 60  # Frames per second

# Colors (R, G, B)
BLACK = (0, 0, 0)

# ---------------------------
# Setup Window and Clock
# ---------------------------
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

# ---------------------------
# Main Loop
# ---------------------------
running = True
while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Drawing ---
    screen.fill(BLACK)  # Fill the screen with black

    # --- Update Display ---
    pygame.display.flip()

    # --- Frame Rate Control ---
    clock.tick(FPS)

# --- Cleanup ---
pygame.quit()
sys.exit()
