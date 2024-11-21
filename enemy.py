from game_settings import *

frames = []
bat_folder = path.join('resources', 'bat')
for file_name in listdir(bat_folder):
    full_path = path.join(bat_folder, file_name)
    surf = pygame.image.load(full_path).convert_alpha()
    frames.append(surf)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, player, collision_sprites):
        super().__init__(groups)
        self.player = player

        self.frames, self.frames_index = frames,0
        self.image = self.frames[self.frames_index]
        self.animation_speed = 6

        self.rect = self.image.get_rect(center = pos)
        self.collision_sprites = collision_sprites
        self.direction = pygame.Vector2()
        self.speed = 300

    def animate(self, dt):
        self.frames_index += self.animation_speed * dt
        self.image = self.frames[int(self.frames_index) % len(self.frames)]

    def move(self, dt):
        player_pos = pygame.Vector2(self.player.rect.center)
        enemy_pos = pygame.Vector2(self.rect.center)
        self.vector = player_pos - enemy_pos
        if self.vector.length() != 0:
            self.direction = self.vector.normalize()
        else:
            self.direction = self.vector

        self.hitbox_rect.centerx += self.direction.x * self.speed * dt
        self.collisions('horizontal')
        self.hitbox_rect.centery += self.direction.y * self.speed * dt
        self.collisions('vertical')
        self.rect.center = self.hitbox_rect.center

    def collisions(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.rect.bottom = sprite.rect.top


    def update(self, dt):
        self.move(dt)
        self.animate(dt)


