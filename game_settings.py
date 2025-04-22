# ---------------------------
# importing libraries
# ---------------------------

import pygame
from os.path import join
from os import walk
from os import path
from os import listdir
import sys
from pytmx.util_pygame import load_pygame
from random import randint
import time

pygame.init()

# ---------------------------
# Configuration Parameters
# ---------------------------

WINDOW_WIDTH, WINDOW_HEIGHT = 1024 ,768
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
TILE_SIZE = 32
button_color = (255, 255, 255)
FONT_SIZE = 20

# ---------------------------
# maps
# ---------------------------

maps = {}
for dirpath, dirnames, filenames in walk(path.join('resources', 'world')):
    for filename in filenames:
        if filename.lower().endswith('.tmx'):
            maps[(filename.split('.')[0])] = (load_pygame(path.join('resources','world',filename)))

# ---------------------------
# bats images
# ---------------------------

bat_frames = []
bat_folder = path.join('resources', 'bat')
for file_name in listdir(bat_folder):
    full_path = path.join(bat_folder, file_name)
    surf = pygame.image.load(full_path).convert_alpha()
    bat_frames.append(surf)

# ---------------------------
# scheletons images
# ---------------------------

scheleton_frames = []
scheleton_folder = path.join('resources', 'skeleton')
for file_name in listdir(scheleton_folder):
    full_path = path.join(scheleton_folder, file_name)
    surf = pygame.image.load(full_path).convert_alpha()
    scheleton_frames.append(surf)

# ---------------------------
# flames images
# ---------------------------

flame_frames = []
flame_folder = path.join('resources', 'torch')
for file_name in listdir(flame_folder):
    full_path = path.join(flame_folder, file_name)
    surf = pygame.image.load(full_path).convert()
    surf.set_colorkey((10,5,46))
    flame_frames.append(surf)

# ---------------------------
# player flame images
# ---------------------------

player_flame_frames = []
player_flame_folder = path.join('resources', 'player_flame')
for file_name in listdir(player_flame_folder):
    full_path = path.join(player_flame_folder, file_name)
    surf = pygame.image.load(full_path).convert()
    surf.set_colorkey((0,0,0))
    player_flame_frames.append(surf)

# ---------------------------
# bonus game images
# ---------------------------

chest = pygame.image.load(path.join('resources','world','chest.png')).convert_alpha()
wall =  pygame.image.load(path.join('resources','world','wall_two.png')).convert_alpha()
# ---------------------------
# rendering images
# ---------------------------

def rendering(text,x,y,FONT_SIZE,display_surface,button_color):
    FONT = pygame.font.SysFont('Georgia', FONT_SIZE)
    text_surface = FONT.render(text, True, button_color)
    text_rect = display_surface.get_rect(center=(x,y))
    display_surface.blit(text_surface, text_rect)

