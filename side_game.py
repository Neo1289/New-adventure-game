from game_settings import *
from sprites import *
from player import *
from groups import allSprites

class SideGame():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.map = maps['maze']
        self.all_sprites = allSprites()
        self.collision_sprites = pygame.sprite.Group()
    def mapping(self):
        for x, y, image in self.map.get_layer_by_name('ground').tiles():
            GroundSprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        for obj in self.map.get_layer_by_name('objects'):
            if obj.image:
                CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in self.map.get_layer_by_name('areas'):
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)

    def run(self):
        dt = self.clock.tick() / 7000
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            display_surface.fill((0, 0, 0))
            self.all_sprites.draw(self.player.rect.center)
            self.all_sprites.update(dt)
            pygame.display.update()

        pygame.quit()
        sys.exit()

