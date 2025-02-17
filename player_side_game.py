from game_settings import (pygame,
                           load_pygame,
                           WINDOW_WIDTH,
                           WINDOW_HEIGHT,
                           sys,
                           join,
                           walk,
                           path)

class PlayerSide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = self.load_images()
        self.image = self.images['right'][0]
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 20))
        self.speed = 3
        self.walk_count = 0
        self.vertical_velocity = 0
        self.is_jumping = False

    def load_images(self):
        self.frames = {'left': [], 'right': []}
        for state in self.frames.keys():
            for folder, subfolder, file_names in walk(path.join('resources', 'player', state)):
                if file_names:
                    for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                        full_path = join(folder, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)
        return self.frames

    def update(self,dt):
        self.keys = pygame.key.get_pressed()
        dt_seconds = dt / 1000.0
        if self.keys[pygame.K_LEFT]:
            self.rect.x -= self.speed * dt_seconds
            self.image = self.images['left'][self.walk_count // 20 % 2]
            self.walk_count += 1
        elif self.keys[pygame.K_RIGHT]:
            self.rect.x += self.speed * dt_seconds
            self.image = self.images['right'][self.walk_count // 20 % 2]
            self.walk_count += 1
        else:
            self.image = self.images['right'][0]
            self.walk_count = 0
        #jumping
        if not self.is_jumping and self.keys[pygame.K_SPACE]:
            self.is_jumping = True
            self.vertical_velocity = -15
        if self.is_jumping:
            self.rect.y += self.vertical_velocity * dt_seconds * 60
            self.vertical_velocity += 1 * dt_seconds * 60
        if  self.rect.centery >= WINDOW_HEIGHT - 20:
            self.rect.bottom = WINDOW_HEIGHT - 20
            self.is_jumping = False
            self.vertical_velocity = 0

