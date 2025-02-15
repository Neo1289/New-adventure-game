from game_settings import (pygame,
                           load_pygame,
                           WINDOW_WIDTH,
                           WINDOW_HEIGHT,
                           display_surface,
                           sys,
                           join,
                           GROUND_FLOOR,
                           walk,
                           path)

class PlayerSide(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.images = self.load_images()
        self.image = self.images['right'][0]
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH //2,GROUND_FLOOR))
        self.speed = 4
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

    def update(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.image = self.images['left'][self.walk_count // 10 % 2]
            self.walk_count += 1
        elif self.keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.image = self.images['right'][self.walk_count // 10 % 2]
            self.walk_count += 1
        else:
            self.image = self.images['left']
            self.walk_count = 0
        #jumping
        if not self.is_jumping and self.keys[pygame.K_SPACE]:
            self.is_jumping = True
            self.vertical_velocity = -15
        if self.is_jumping:
            self.rect.y += self.vertical_velocity
            self.vertical_velocity += 1
        if  self.rect.centery >= GROUND_FLOOR:
            self.rect.bottom = GROUND_FLOOR
            self.is_jumping = False
            self.vertical_velocity = 0
