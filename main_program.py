import random

from game_settings import (pygame,
                           maps,
                           display_surface,
                           WINDOW_HEIGHT, WINDOW_WIDTH,
                           TILE_SIZE, FONT_SIZE,
                           button_color,
                           sys, bat_frames, scheleton_frames, chest, rendering, flame_frames,player_flame_frames)
from player import Player
from sprites import GroundSprite, CollisionSprite, AreaSprite, BonusSprite, Wall, ColumnSprite,Rune
from groups import allSprites
from enemy import Enemy
from flame import Flame, PlayerFlame
from side_game import SideGame
from menu import GameMenu
from storyteller import StoryTeller

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
        self.FONT_SIZE = FONT_SIZE

        ###groups
        self.all_sprites = allSprites()
        self.collision_sprites = pygame.sprite.Group()
        ###extra monsters
        self.monster_event = pygame.event.custom_type()
        pygame.time.set_timer(self.monster_event, 5000)
        self.bonus_event = pygame.event.custom_type()
        pygame.time.set_timer(self.bonus_event, 7000)
        self.wall_event = pygame.event.custom_type()
        pygame.time.set_timer(self.wall_event, 1000)
        self.transition = False
        self.finding = None
        self.inventory = None
        self.secret = False

        #### game objects that can be used by the player
        self.game_objects = {
            'potion': 1,
            'crystal ball': 1,
            'coin': 0
        }
        self.keys_list = list(self.game_objects.keys())
        self.last_object_found = ''

    def setup(self):
        self.all_sprites.empty()
        self.collision_sprites.empty()
        self.area_groups.clear()

        for name, map in self.maps.items():
            if name == self.current_area:
                self.current_map = map

    def mapping(self):
        self.inventory = False ###giving the change to trade until in the room
        ###ground tiles###
        for x, y, image in self.current_map.get_layer_by_name('ground').tiles():
            GroundSprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        ###objects###

        for obj in self.current_map.get_layer_by_name('objects'):
            if obj.image and obj.name != 'runes':
                CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites), obj.name)
            else:
                ColumnSprite((obj.x,obj.y),obj.image,(self.all_sprites, self.collision_sprites), obj.name)

        ###player###

        for obj in self.current_map.get_layer_by_name('areas'):
            if obj.name == 'player_spawn':
                if self.player is None:
                    self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
                    self.player.game = self
                else:
                    self.player.collision_rect.center = (obj.x, obj.y)
                    self.all_sprites.add(self.player)
                    self.player.game = self

            elif obj.name not in ('bat','scheleton','wall','flame'):
                self.area_groups[obj.name] = AreaSprite(obj.x, obj.y, obj.width, obj.height, self.all_sprites)

    def monsters(self):
        ###spawning monsters
        for obj in self.current_map.get_layer_by_name('areas'):
            if obj.name == 'bat':
                self.monster = Enemy((obj.x,obj.y), bat_frames, self.all_sprites)
            elif obj.name == 'scheleton':
                self.scheleton = Enemy((obj.x, obj.y), scheleton_frames, self.all_sprites)
            elif obj.name == 'flame':
                self.flame = Flame((obj.x, obj.y), flame_frames, self.all_sprites)

    def wall_spawn(self):
            walls = [obj for obj in self.current_map.get_layer_by_name('areas')
                     if obj.name == 'wall']
            if walls:
                chosen_wall = random.choice(walls)
                self.wall = Wall(chosen_wall.x,chosen_wall.y,self.all_sprites)

    def bonus_game(self):
        bonus_objects = [obj for obj in self.current_map.get_layer_by_name('areas')
                         if obj.name == 'spawning bonus']

        if bonus_objects:
            chosen_obj = random.choice(bonus_objects)
            self.bonus = BonusSprite((chosen_obj.x, chosen_obj.y), chest,
                                         (self.all_sprites, self.collision_sprites), chosen_obj.name, 3000)

    # New helper method for rendering text
    def _render_text(self, text, x, y):
        rendering(text, x, y, self.FONT_SIZE, self.display_surface, button_color)

    def render(self):
        #display next stage
        for name, area in self.area_groups.items():
            if area.rect.colliderect(self.player.rect) and name == 'secret passage':
                self.text = f"You found a {name} press Y to enter"
                self._render_text(self.text, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
                self.current_area = name
            elif area.rect.colliderect(self.player.rect) and name == 'secret game':
                self.text = f"Press Y to enter the {name}"
                self._render_text(self.text, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
                self.secret = True
            elif area.rect.colliderect(self.player.rect):
                self.text = f"Press Y to enter the {name}"
                self._render_text(self.text,WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
                self.current_area = name

        for obj in self.collision_sprites:
            if obj.rect.colliderect(self.player.rect) and obj.name != None and obj.resources == 1:
                if obj.name not in ('merchant','runes'):
                    self.text = f"do you want inspect the {obj.name}?"

                rendering(self.text, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, FONT_SIZE, self.display_surface, button_color)

            if obj.name == 'merchant' and obj.rect.colliderect(self.player.rect):
                self.text = ("do you want to sell your crystal balls? \n"
                                     "Press E to see your tradable resources. S to sell \n"
                                     "B to buy potions")

                rendering(self.text, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, FONT_SIZE, self.display_surface, button_color)

            if self.inventory and obj.rect.colliderect(self.player.rect) and obj.name == 'merchant':
                self.inventory_font = self.FONT_SIZE
                for key, value in self.game_objects.items():
                    self.text_inv = f"you have {value} {key}"
                    rendering(self.text_inv, self.player.rect.centerx - 100,
                              self.player.rect.centery - 100 - self.inventory_font, FONT_SIZE, self.display_surface,
                              button_color)
                    self.inventory_font += self.FONT_SIZE

            if obj.rect.colliderect(self.player.rect) and obj.name == 'runes':
                if self.player.runes_found < 3:
                    self.text = "do you want to collect the energy of the runes?"
                    rendering(self.text, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, FONT_SIZE, self.display_surface, button_color)
                else:
                    self.text = "You have too much runes energy, you can't collect more"
                    rendering(self.text, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, FONT_SIZE, self.display_surface, button_color)

    def transition_check(self,event): ###check if the player is in an area for transition and if the y has been pressed
        for name, area in self.area_groups.items():
            if (area.rect.colliderect(self.player.rect)
                    and event.type == pygame.KEYDOWN
                    and event.key == pygame.K_y):
                self.transition = True

        for obj in self.collision_sprites:
            if obj.rect.colliderect(self.player.rect) and obj.name != None and event.type == pygame.KEYDOWN and event.key == pygame.K_y and obj.resources == 1 and obj.name not in ('merchant'):
                self.finding = random.randint(0,2)

                for i in range(len(self.keys_list)):
                    if i == self.finding and obj.name != 'runes':
                        key = self.keys_list[self.finding]
                        self.game_objects[key] += 1
                        self.last_object_found = self.keys_list[i]
                        self.finding = None
                        obj.resources = 0
                    elif obj.name == 'runes' and self.player.runes_found < 3:
                        obj.resources = 0
                        self.player.runes_found += 1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_e and obj.rect.colliderect(self.player.rect) and obj.name == 'merchant':
                    self.inventory = True

    def using_resources(self,event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            if self.game_objects['potion'] > 0:
                self.player.life = 100
                self.game_objects['potion'] -= 1

    def trading_resouces(self,event):
        if self.inventory:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s and self.game_objects['crystal ball'] > 0:
                self.game_objects['crystal ball'] -= 1
                self.game_objects['coin'] += 5
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b and self.game_objects['coin'] >= 3:
                self.game_objects['coin'] -= 3
                self.game_objects['potion'] += 1

    def remapping(self): ###check if bool is true and perform the remapping
        if self.transition and not self.secret:
            self.setup()
            self.mapping()
            self.transition = False
            self.story_teller = StoryTeller(self.current_area)
            self.story_teller.run()
        elif self.transition and self.secret:
            side_game = SideGame()
            side_game.run()
            self.transition = False
            self.secret = False
            if side_game.platform_player.coins_collected > 30:
                self.game_objects['potion'] += 1
                self.last_object_found = 'you collected more than 30 coins you get a potion!'

    def player_life_check(self):
        for sprite in self.all_sprites:
            if hasattr(sprite, "dangerous"):
                if sprite.rect.colliderect(self.player):
                    self.player.life -= 1

        if self.player.life <= 0:
            self.caption = pygame.display.set_caption('GAME OVER')
            pygame.time.delay(10000)
            pygame.quit()
            sys.exit()

    def display_captions(self):
        time_sec = pygame.time.get_ticks() // 1000
        self.caption = (f"\u2665 {self.player.life}      "
                   f"\U0001F9EA {self.game_objects['potion']}      "
                   f"\U0001F52E {self.game_objects['crystal ball']}     "
                   f"\U0001F4B0 {self.game_objects['coin']}       "
                   f"runes dust: {self.player.runes_found}       "
                   f"time: {time_sec}         "
                   f"last object found: {self.last_object_found}    " 
                   )
        pygame.display.set_caption(self.caption)

    def check_rune_collisions(self):
        enemies = [sprite for sprite in self.all_sprites if isinstance(sprite, Enemy)]
        rune_group = pygame.sprite.Group([sprite for sprite in self.all_sprites if isinstance(sprite, (Rune))])
        flame_group = pygame.sprite.Group(
            [sprite for sprite in self.all_sprites if isinstance(sprite, (PlayerFlame))])

        for enemy in enemies:
            rune_hits = pygame.sprite.spritecollide(enemy, rune_group, False)
            flame_hits = pygame.sprite.spritecollide(enemy, flame_group, False)
            if rune_hits:
                enemy.kill()
            elif flame_hits:
                enemy.kill()
                PlayerFlame((self.player.rect.centerx,self.player.rect.centery), player_flame_frames, self.all_sprites)

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.monster_event:
                    self.monsters()
                if event.type == self.bonus_event:
                    self.bonus_game()
                if event.type == self.wall_event:
                    self.wall_spawn()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.player.shoot(self.all_sprites)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                    self.player.shoot_fire(groups=self.all_sprites)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    self.menu_item = GameMenu(objects=main_game.game_objects)
                    self.menu_item.run()

                self.transition_check(event)
                self.using_resources(event)
                self.trading_resouces(event)

            self.remapping()
            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            self.all_sprites.update(dt)
            self.check_rune_collisions()
            self.render()
            self.player_life_check()
            self.display_captions()
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    main_game = Game()
    menu_item = GameMenu(objects=main_game.game_objects)
    menu_item.run()
    main_game.setup()
    main_game.mapping()
    main_game.monsters()
    main_game.run()
