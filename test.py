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
running = True

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

#---------------------------
#testing code
#---------------------------
all_sprites = pygame.sprite.Group()

enemy = Enemy((400,300),frames,all_sprites)

# running = True
while running:
    dt = clock.tick(FPS) /1000
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Drawing ---
    screen.fill(BLACK)  # Fill the screen with black

    all_sprites.update(dt)
    all_sprites.draw(screen)
    # --- Update Display ---
    pygame.display.flip()

# --- Cleanup ---
pygame.quit()
sys.exit()
