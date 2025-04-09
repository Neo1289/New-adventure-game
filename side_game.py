from game_settings import (display_surface,
                           pygame,
                           sys,
                           join
                           )
from player import Player


class Platform(Player):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(pos, groups, collision_sprites)
        # Physics variables for jumping
        self.gravity = 0.8
        self.jump_power = -15
        self.velocity_y = 0
        self.is_jumping = False
        self.on_ground = True

        # Get screen dimensions for boundary checking
        self.screen_width = pygame.display.get_surface().get_width()
        self.screen_height = pygame.display.get_surface().get_height()

    def input(self):
        # Use the horizontal movement from parent class
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])
        if self.direction.length() > 0:  # Prevent division by zero
            self.direction = self.direction.normalize()

        # Add jump input
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_power
            self.is_jumping = True
            self.on_ground = False

    def move(self, dt):
        # Handle horizontal movement using parent method
        self.collision_rect.x += self.direction.x * self.speed * dt
        self.handle_collision('horizontal')

        # Apply screen boundaries for horizontal movement
        self.apply_horizontal_boundaries()

        self.rect.centerx = self.collision_rect.centerx

        # Apply gravity and handle vertical movement
        self.velocity_y += self.gravity
        self.collision_rect.y += self.velocity_y
        self.handle_platform_collision()

        # Apply screen boundaries for vertical movement
        self.apply_vertical_boundaries()

        self.rect.centery = self.collision_rect.centery

    def apply_horizontal_boundaries(self):
        # Left boundary
        if self.collision_rect.left < 0:
            self.collision_rect.left = 0

        # Right boundary
        if self.collision_rect.right > self.screen_width:
            self.collision_rect.right = self.screen_width

    def apply_vertical_boundaries(self):
        # Top boundary
        if self.collision_rect.top < 0:
            self.collision_rect.top = 0
            self.velocity_y = 0  # Stop upward movement if hitting the ceiling

        # Bottom boundary (typically handled by platform collision,
        # but this is a safety measure)
        if self.collision_rect.bottom > self.screen_height:
            self.collision_rect.bottom = self.screen_height
            self.velocity_y = 0
            self.on_ground = True
            self.is_jumping = False

    def handle_platform_collision(self):
        self.on_ground = False
        for platform in self.game.platforms:
            platform_rect = pygame.Rect(platform)

            # Check if falling onto platform
            if self.velocity_y > 0 and self.collision_rect.bottom >= platform_rect.top and self.collision_rect.bottom <= platform_rect.top + 20:
                if self.collision_rect.right > platform_rect.left and self.collision_rect.left < platform_rect.right:
                    self.collision_rect.bottom = platform_rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                    self.is_jumping = False


class SideGame():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.display_surface = display_surface
        self.platform_group = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # Get screen dimensions
        self.screen_width = self.display_surface.get_width()
        self.screen_height = self.display_surface.get_height()

        # Create more varied platforms
        self.platforms = [
            # Ground platform
            [0, self.screen_height - 50, self.screen_width, 20],

            # Left side platforms (stair-like arrangement)
            [50, self.screen_height - 150, 200, 20],
            [150, self.screen_height - 250, 180, 20],
            [50, self.screen_height - 350, 160, 20],
            [150, self.screen_height - 450, 140, 20],

            # Central platforms
            [400, self.screen_height - 200, 180, 20],
            [350, self.screen_height - 350, 150, 20],
            [450, self.screen_height - 500, 120, 20],

            # Right side platforms
            [600, self.screen_height - 120, 200, 20],
            [650, self.screen_height - 240, 180, 20],
            [700, self.screen_height - 360, 160, 20],
            [650, self.screen_height - 480, 140, 20],

            # Small challenging platforms
            [300, self.screen_height - 300, 80, 20],
            [500, self.screen_height - 400, 80, 20],
            [380, self.screen_height - 580, 70, 20],

            # High reward platforms
            [280, 100, 120, 20],  # Very high platform
            [550, 150, 100, 20],  # High platform on right
            [100, 120, 100, 20],  # High platform on left
        ]

        # Player starts near the ground
        self.platform_player = Platform((100, self.screen_height - 100), self.platform_group, self.collision_sprites)
        self.platform_player.game = self  # Pass reference to game instance

        self.ground_rect = pygame.Rect(0, self.screen_height - 50, self.screen_width, 50)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)

        # More varied platform colors
        self.GROUND_COLOR = (100, 50, 0)  # Brown for ground
        self.PLATFORM_COLORS = [
            (0, 200, 0),  # Green
            (0, 150, 100),  # Teal
            (100, 100, 250)  # Light purple
        ]

        # Background
        self.bg_color = (20, 20, 40)  # Dark blue-ish background

    def draw_platforms(self):
        # Draw ground platform with ground color
        pygame.draw.rect(self.display_surface, self.GROUND_COLOR, self.platforms[0])

        # Draw other platforms with alternating colors
        for i, platform in enumerate(self.platforms[1:], 1):
            color_index = i % len(self.PLATFORM_COLORS)
            pygame.draw.rect(self.display_surface, self.PLATFORM_COLORS[color_index], platform)

    def display_instructions(self):
        # Create a font for instructions
        font = pygame.font.SysFont('Arial', 18)
        text = font.render("Use Arrow Keys/WASD to move, SPACE to jump, ESC to exit", True, self.WHITE)
        self.display_surface.blit(text, (20, 20))

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

            # Clear screen with background color
            self.display_surface.fill(self.bg_color)

            # Draw instructions
            self.display_instructions()

            # Draw platforms
            self.draw_platforms()

            # Update and draw player
            self.platform_group.update(dt)
            self.platform_group.draw(self.display_surface)

            pygame.display.update()

        return