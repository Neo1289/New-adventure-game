import pygame.surface
from game_settings import *
from player import *
from sprites import *
from groups import allSprites

class Game:
    def __init__(self):
        self.running = True
        self.display_surface = display_surface
        self.clock = pygame.time.Clock()
        self.maps = maps
        self.current_area = 'world_map'
        self.current_map = None
        self.area_groups = {}
        self.entry = False
        #groups
        self.all_sprites = allSprites()
        self.collision_sprites = pygame.sprite.Group()

    def setup(self):
        self.all_sprites.empty()
        self.collision_sprites.empty()

        for name, map in self.maps.items():
            if name == self.current_area:
                self.current_map = map

    def mapping(self):
        [GroundSprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites) for x, y, image in
        self.current_map.get_layer_by_name('ground').tiles() if self.current_map.get_layer_by_name('ground')]

        if self.current_map.get_layer_by_name('objects'):
            for obj in self.current_map.get_layer_by_name('objects'):
                if obj.image:
                    CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        if self.current_map.get_layer_by_name('areas'):
            for obj in self.current_map.get_layer_by_name('areas'):
                if obj.name != 'player_spawn':
                    self.area_groups[obj.name] = AreaSprite(obj.x, obj.y, obj.width, obj.height, self.all_sprites)
                elif obj.name == 'player_spawn':
                    self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)

    def question(self):
        for name, area in self.area_groups.items():
            if area.rect.colliderect(self.player.rect):
                self.FONT = pygame.font.SysFont('Georgia', FONT_SIZE)
                self.text = f"Press Y to enter the {name}"
                self.text_surface = self.FONT.render(self.text, True, button_color)
                self.text_rect = display_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                self.display_surface.blit(self.text_surface, self.text_rect)
                self.current_area = name
                self.entry = True

    def run(self):
        while self.running:
            dt = self.clock.tick() / 3000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN and event.key == pygame.K_y and self.entry:
                    self.setup()
                    self.mapping()
                    self.entry = False

            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            self.all_sprites.update(dt)
            self.question()
            print(self.current_area)
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.setup()
    game.mapping()
    game.run()