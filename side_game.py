from game_settings import *
from sprites import *
from player import *
from groups import allSprites
from main_program import Game
from enemy import *

class SideGame():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.map = maps['maze']
        self.all_sprites = allSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bat_event = pygame.event.custom_type()
        pygame.time.set_timer(self.bat_event, 4000)

    def mapping(self):
        for x, y, image in self.map.get_layer_by_name('ground').tiles():
            GroundSprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        for obj in self.map.get_layer_by_name('objects'):
            if obj.image:
                CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in self.map.get_layer_by_name('areas'):
            if obj.name == 'shrine':
                self.shrine_sprite = AreaSprite(obj.x, obj.y, obj.width, obj.height, self.all_sprites)
            elif obj.name == 'player_spawn':
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
            elif obj.name == 'monster':
                self.monster = Enemy((obj.x,obj.y),frames,self.all_sprites)

    def customer_mapping(self):
        for obj in self.map.get_layer_by_name('areas'):
            if obj.name == 'monster':
                self.monster = Enemy((obj.x,obj.y),frames,self.all_sprites)

    def run(self):
        dt = self.clock.tick() / 7000
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    game = Game()
                    game.current_area = 'forest'
                    game.setup()
                    game.mapping()
                    game.run()
                if event.type == self.bat_event:
                    self.customer_mapping()

            for sprite in self.all_sprites:
                if hasattr(sprite, "sprite_type"):
                    if sprite.rect.colliderect(self.player):
                        print('ok')

            display_surface.fill((0, 0, 0))
            self.all_sprites.draw(self.player.rect.center)
            self.all_sprites.update(dt)

            if self.shrine_sprite.rect.colliderect(self.player.rect):
                self.FONT = pygame.font.SysFont('Georgia', FONT_SIZE)
                self.text = "Press Y to exit the Shrine"
                self.text_surface = self.FONT.render(self.text, True, button_color)
                self.text_rect = display_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                display_surface.blit(self.text_surface, self.text_rect)

            pygame.display.update()

        pygame.quit()
        sys.exit()

