from game_settings import *
from sprites import Rune
from flame import PlayerFlame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups, collision_sprites):
        super().__init__(groups)
        self.load_images()
        self.state, self.frame_index = 'down', 0
        self.image = pygame.image.load(join('resources','player','down','0.png')).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.collision_rect = self.rect.inflate(-30, -30)
        self.direction = pygame.Vector2(0,0)
        self.speed = 200
        self.groups = groups
        self.collision_sprites = collision_sprites
        self.life = 100
        self.runes_found = 0

    def input(self):
        self.keys = pygame.key.get_pressed()
        self.direction.x = int(self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]) - int(self.keys[pygame.K_LEFT] or self.keys[pygame.K_a])
        self.direction.y = int(self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]) - int(self.keys[pygame.K_UP] or self.keys[pygame.K_w])
        if self.direction.length() > 0:  # Prevent division by zero
            self.direction = self.direction.normalize()

    def move(self, dt):
        self.collision_rect.x += self.direction.x * self.speed * dt
        self.handle_collision('horizontal')
        self.rect.centerx = self.collision_rect.centerx

        self.collision_rect.y += self.direction.y * self.speed * dt
        self.handle_collision('vertical')
        self.rect.centery = self.collision_rect.centery

    def handle_collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.collision_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0:  # Moving right
                        self.collision_rect.right = sprite.rect.left
                    if self.direction.x < 0:  # Moving left
                        self.collision_rect.left = sprite.rect.right
                elif direction == 'vertical':
                    if self.direction.y > 0:  # Moving down
                        self.collision_rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # Moving up
                        self.collision_rect.top = sprite.rect.bottom

    def load_images(self):
        self.frames = {'left': [], 'right': [], 'up': [], 'down': []}
        for state in self.frames.keys():
            for folder, subfolder, file_names in walk(path.join('resources', 'player', state)):
                if file_names:
                    for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                        full_path = join(folder, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)

    def animate(self, dt):
        if self.direction.x != 0:
            self.state = 'right' if self.direction.x > 0 else 'left'
        if self.direction.y != 0:
            self.state = 'down' if self.direction.y > 0 else 'up'

        self.frame_index = self.frame_index + 10 * dt if self.direction else 0
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]

    def shoot(self, groups):

        if self.runes_found > 0:
            Rune(self.rect.center, groups)
            self.runes_found -= 1

    def shoot_fire(self, groups):
        if self.runes_found == 3:
            PlayerFlame((self.rect.centerx,self.rect.centery), flame_frames,groups)
            self.runes_found = 0

    def update(self,dt):
        self.input()
        self.move(dt)
        self.animate(dt)
