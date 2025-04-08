import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platform Jumping Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Player properties
player_width = 40
player_height = 60
player_x = 50
player_y = SCREEN_HEIGHT - player_height - 10
player_vel_x = 0
player_vel_y = 0
player_speed = 5
player_jump = -15
gravity = 0.8

# Platforms - each platform is [x, y, width, height]
platforms = [
    [0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, 10],  # Ground
    [100, 400, 200, 20],  # Platform 1
    [400, 300, 150, 20],  # Platform 2
    [250, 200, 100, 20],  # Platform 3
    [550, 150, 200, 20]  # Platform 4
]

# Game variables
running = True
clock = pygame.time.Clock()


def draw_player(x, y):
    """Draw the player character"""
    pygame.draw.rect(SCREEN, BLUE, (x, y, player_width, player_height))


def draw_platforms():
    """Draw all platforms"""
    for platform in platforms:
        pygame.draw.rect(SCREEN, GREEN, platform)


def check_collision(player_rect, platforms):
    """Check for collision between player and platforms"""
    for platform in platforms:
        platform_rect = pygame.Rect(platform)
        if player_rect.colliderect(platform_rect):
            return True
    return False


def main_game():
    global player_x, player_y, player_vel_x, player_vel_y, running

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_vel_x = -player_speed
                if event.key == pygame.K_RIGHT:
                    player_vel_x = player_speed
                if event.key == pygame.K_SPACE:
                    # Check if player is on ground or platform before jumping
                    player_rect = pygame.Rect(player_x, player_y + 1, player_width, player_height)
                    if check_collision(player_rect, platforms):
                        player_vel_y = player_jump

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    player_vel_x = 0

        # Update player position
        player_x += player_vel_x
        player_y += player_vel_y
        player_vel_y += gravity

        # Check boundaries
        if player_x < 0:
            player_x = 0
        if player_x > SCREEN_WIDTH - player_width:
            player_x = SCREEN_WIDTH - player_width

        # Check platform collisions for vertical movement
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

        # Bottom collision (landing on platforms)
        if player_vel_y > 0:
            player_rect_bottom = pygame.Rect(player_x, player_y + player_vel_y, player_width, player_height)
            for platform in platforms:
                platform_rect = pygame.Rect(platform)
                if player_rect_bottom.colliderect(platform_rect) and player_rect.bottom <= platform_rect.top:
                    player_y = platform_rect.top - player_height
                    player_vel_y = 0

        # Top collision (hitting head on platforms)
        if player_vel_y < 0:
            player_rect_top = pygame.Rect(player_x, player_y + player_vel_y, player_width, player_height)
            for platform in platforms:
                platform_rect = pygame.Rect(platform)
                if player_rect_top.colliderect(platform_rect) and player_rect.top >= platform_rect.bottom:
                    player_y = platform_rect.bottom
                    player_vel_y = 0

        # Draw everything
        SCREEN.fill(WHITE)
        draw_platforms()
        draw_player(player_x, player_y)

        # Update display
        pygame.display.update()
        clock.tick(60)  # 60 FPS


if __name__ == "__main__":
    main_game()