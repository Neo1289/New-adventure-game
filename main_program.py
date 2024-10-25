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
        self.area_list = []
        self.area_names = []
        self.level = []

        #groups
        self.all_sprites = allSprites()
        self.collision_sprites = pygame.sprite.Group()

    def setup(self):
        map = load_pygame(join('resources','world','world_map.tmx'))

        #####BACKGROUND TILES --> self.ground = True

        for x, y, image in map.get_layer_by_name('ground').tiles():
            GroundSprite((x * TILE_SIZE,y * TILE_SIZE),image,self.all_sprites)

        for x,y, image in map.get_layer_by_name('grass').tiles():
                GroundSprite((x * TILE_SIZE,y * TILE_SIZE),image,self.all_sprites)

        for x, y, image in map.get_layer_by_name('stoneGround').tiles():
                GroundSprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        #####CHARACTERS AND OBJECTS --> self.groud = False
        for obj in map.get_layer_by_name('trees'):
            if obj.image:
                CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in map.get_layer_by_name('rocks_and_props'):
            if obj.image:
                CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

                #=============
                ##area sprites
                #=============

        for obj in map.get_layer_by_name('areas'):
            self.area_sprite = AreaSprite(obj.x, obj.y, obj.width, obj.height, self.all_sprites)
            self.area_list.append(self.area_sprite)
            self.area_names.append(obj.name)

        #==========
        #PLAYER====
        #==========

        for obj in map.get_layer_by_name('entities_spawn'):
            if obj.name == 'player_spawn':
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)

    def areas(self):
        for i in range(len(self.area_list)):
            if self.area_list[i].rect.colliderect(self.player.rect):
                self.FONT = pygame.font.SysFont('Georgia', FONT_SIZE)
                self.text = f"Press Y to enter the {self.area_names[i]}"
                self.text_surface = self.FONT.render(self.text, True, button_color)
                self.text_rect = display_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                self.display_surface.blit(self.text_surface, self.text_rect)
                self.level.append(self.area_names[i])

    def run(self):
        while self.running:
            dt = self.clock.tick() / 3000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y and self.level:
                        print(f"Key pressed: {self.level}")

            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            self.all_sprites.update(dt)
            self.areas()
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.setup()
    game.run()