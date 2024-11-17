import pygame.surface
from game_settings import *
from player import *
from sprites import *
from groups import allSprites
from side_game import *

class Game:
    def __init__(self):
        self.running = True
        self.display_surface = display_surface
        self.clock = pygame.time.Clock()
        self.maps = maps
        self.current_area = 'world_map'
        self.current_map = None
        self.player = None
        self.area_groups = {}
        #groups
        self.all_sprites = allSprites()
        self.collision_sprites = pygame.sprite.Group()

    def display_time(self):
        self.current_time = pygame.time.get_ticks() // 1000
        self.current_time = str(self.current_time)
        self.font = pygame.font.SysFont('Georgia', 20)
        self.text_surf = self.font.render(self.current_time, True, (250, 235, 240))
        self.text_rect = self.text_surf.get_rect(bottomright = (WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
        self.display_surface.blit(self.text_surf, self.text_rect)

    def setup(self):
        self.all_sprites.empty()
        self.collision_sprites.empty()
        self.area_groups.clear()

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

    def run(self):
        while self.running:
            dt = self.clock.tick() / 3000
            global shrine
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type ==  pygame.KEYDOWN and event.key == pygame.K_y and self.current_area != 'shrine':
                    self.setup()
                    self.mapping()
                elif event.type ==  pygame.KEYDOWN and event.key == pygame.K_y and self.current_area == 'shrine':
                    print('Entering Shrine...')
                    self.running = False
                    shrine_game = SideGame()
                    shrine_game.mapping()
                    shrine_game.run()

            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            self.question()
            self.all_sprites.update(dt)
            self.display_time()
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.setup()
    game.mapping()
    game.run()