import pygame


def run_minigame(screen):
    # Create a separate clock for the minigame
    clock = pygame.time.Clock()
    running = True

    # Example minigame variables
    font = pygame.font.Font(None, 36)
    text = font.render("Minigame: Press ESC to return", True, (255, 255, 255))
    background_color = (0, 0, 100)  # Different background color for minigame

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Exit minigame and return to main game

        # Minigame logic and rendering
        screen.fill(background_color)  # Fill the screen with minigame color
        screen.blit(text, (150, screen.get_height() // 2))

        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

    # Optional: Display a message in the main game after returning
    display_return_message(screen)


def display_return_message(screen):
    font = pygame.font.Font(None, 36)
    message = font.render("Returned to Main Game!", True, (255, 255, 255))
    screen.blit(message, (250, screen.get_height() // 2 + 50))
    pygame.display.flip()
    pygame.time.delay(1000)  # Display the message for 1 second
