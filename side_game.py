from game_settings import (display_surface,
                           pygame,
                           maps,
                           TILE_SIZE,
                           FONT_SIZE,
                           WINDOW_WIDTH,WINDOW_HEIGHT,
                           button_color,
                           sys)
from sprites import GroundSprite,CollisionSprite,AreaSprite
from player import Player
from groups import allSprites
from enemy import Enemy,frames

class SideGame():
    def __init__(self,player):
        self.running = True
        self.clock = pygame.time.Clock()
        self.map = maps['maze']
        self.all_sprites = allSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bat_event = pygame.event.custom_type()
        pygame.time.set_timer(self.bat_event, 1000)
        self.player = player

    def custom_mapping(self):
        for obj in self.map.get_layer_by_name('areas'):
            if obj.name == 'monster':
                self.monster = Enemy((obj.x,obj.y),frames,self.all_sprites)

    def run(self):
        dt = self.clock.tick() / 10000
        self.all_sprites.add(self.player)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.bat_event:
                    self.custom_mapping()

            for sprite in self.all_sprites:
                if hasattr(sprite, "sprite_type"): #identify bats among the sprites
                    if sprite.rect.colliderect(self.player):
                        self.player.life -=1

            display_surface.fill((0, 0, 0))

            if self.shrine_sprite.rect.colliderect(self.player.rect):
                self.FONT = pygame.font.SysFont('Georgia', FONT_SIZE)
                self.text = "Press Y to exit the Shrine"
                self.text_surface = self.FONT.render(self.text, True, button_color)
                self.text_rect = display_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                display_surface.blit(self.text_surface, self.text_rect)

            self.all_sprites.draw(self.player.rect.center)
            self.all_sprites.update(dt)

            self.caption = pygame.display.set_caption(f'Player life {self.player.life}')
            pygame.display.update()

        pygame.quit()
        sys.exit()
