import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Platformer")

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Define colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
GREEN = ( 34,139,  34)

# Player attributes
player_width = 40
player_height = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 50  # Start above the ground
player_speed_x = 0
player_speed_y = 0
move_speed = 5
jump_speed = 15
gravity = 0.8

# Platform
platform_rect = pygame.Rect(0, HEIGHT - 30, WIDTH, 30)

def draw_platform():
    """Draws the ground platform."""
    pygame.draw.rect(screen, GREEN, platform_rect)

def draw_player(x, y):
    """Draws the player as a rectangle."""
    pygame.draw.rect(screen, BLACK, (x, y, player_width, player_height))

def handle_input():
    """Handles left/right input and jump events."""
    global player_speed_x, player_speed_y

    keys = pygame.key.get_pressed()

    # Horizontal movement
    if keys[pygame.K_LEFT]:
        player_speed_x = -move_speed
    elif keys[pygame.K_RIGHT]:
        player_speed_x = move_speed
    else:
        player_speed_x = 0

    # Jumping
    if keys[pygame.K_SPACE]:
        # Only jump if the player is on (or just hitting) the platform
        if player_y + player_height >= platform_rect.top and player_speed_y == 0:
            player_speed_y = -jump_speed

def update_player():
    """Updates the player's position and handles collisions."""
    global player_x, player_y, player_speed_x, player_speed_y

    # Apply horizontal movement
    player_x += player_speed_x

    # Gravity
    player_speed_y += gravity
    player_y += player_speed_y

    # Collision with the platform (simple floor collision)
    if player_y + player_height > platform_rect.top:
        player_y = platform_rect.top - player_height
        player_speed_y = 0

    # Keep player within window horizontally
    if player_x < 0:
        player_x = 0
    if player_x + player_width > WIDTH:
        player_x = WIDTH - player_width

def main():
    """Main game loop."""
    global screen

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input()
        update_player()

        # Drawing
        screen.fill(WHITE)
        draw_platform()
        draw_player(player_x, player_y)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
