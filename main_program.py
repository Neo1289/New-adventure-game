from game_settings import (pygame,
                           maps,
                           display_surface,
                           WINDOW_HEIGHT,WINDOW_WIDTH,
                           TILE_SIZE,FONT_SIZE,
                           button_color,
                           sys, frames)
from player import Player
from sprites import GroundSprite, CollisionSprite, AreaSprite
from groups import allSprites
from enemy import Enemy

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
        ###groups
        self.all_sprites = allSprites()
        self.collision_sprites = pygame.sprite.Group()
        ###extra bats
        self.bat_event = pygame.event.custom_type()
        pygame.time.set_timer(self.bat_event, 3000)
        self.transition = False

    def display_time(self):
        self.current_time = pygame.time.get_ticks() // 100
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

        ###ground tiles###

        for x, y, image in self.current_map.get_layer_by_name('ground').tiles():
            GroundSprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        ###objects###

        for obj in self.current_map.get_layer_by_name('objects'):
            if obj.image:
                CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites),obj.name)

        ###areas and animated characters###

        for obj in self.current_map.get_layer_by_name('areas'):
            if obj.name == 'player_spawn':
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
            elif obj.name == 'monster':
                self.monster = Enemy((obj.x, obj.y), frames, self.all_sprites)
            else:
                self.area_groups[obj.name] = AreaSprite(obj.x, obj.y, obj.width, obj.height, self.all_sprites)

    def custom_mapping(self): ###spawning extra bats
        for obj in self.current_map.get_layer_by_name('areas'):
            if obj.name == 'monster':
                self.monster = Enemy((obj.x,obj.y),frames,self.all_sprites)

    def question(self): ###ask if the player wants to enter the next stage
        for name, area in self.area_groups.items():
            if area.rect.colliderect(self.player.rect):
                self.FONT = pygame.font.SysFont('Georgia', FONT_SIZE)
                self.text = f"Press Y to enter the {name}"
                self.text_surface = self.FONT.render(self.text, True, button_color)
                self.text_rect = display_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
                self.display_surface.blit(self.text_surface, self.text_rect)
                self.current_area = name
        for obj in self.collision_sprites:
            if obj.rect.colliderect(self.player.rect) and obj.name != None:
                self.FONT = pygame.font.SysFont('Georgia', FONT_SIZE)
                self.text = f"do you want inspect the {name}?"
                self.text_surface = self.FONT.render(self.text, True, button_color)
                self.text_rect = display_surface.get_rect(center=(WINDOW_WIDTH / 3,WINDOW_HEIGHT / 3))
                self.display_surface.blit(self.text_surface, self.text_rect)

    def transition_check(self,event): ###check if the player is in an area for transition and if the y has been pressed
        for name, area in self.area_groups.items():
            if area.rect.colliderect(self.player.rect) and event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                self.transition = True

    def transition_performer(self): ###check if bool is true and perform the remapping
        if self.transition:
            self.setup()
            self.mapping()
            self.transition = False

    def player_life_check(self):
        for sprite in self.all_sprites:
            if hasattr(sprite, "bat"):
                if sprite.rect.colliderect(self.player):
                    self.player.life -= 1

        if self.player.life <= 0:
            self.caption = pygame.display.set_caption('GAME OVER')
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

    def run(self):
        while self.running:
            dt = self.clock.tick() / 3000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.bat_event:
                    self.custom_mapping()
                self.transition_check(event)

            self.transition_performer()
            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            self.all_sprites.update(dt)
            self.display_time()
            self.question()
            self.player_life_check()

            pygame.display.set_caption(f'Player life {self.player.life}')
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.setup()
    game.mapping()
    game.run()