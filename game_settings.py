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

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600 ###1024 ,768
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

frames = []
bat_folder = path.join('resources', 'bat')
for file_name in listdir(bat_folder):
    full_path = path.join(bat_folder, file_name)
    surf = pygame.image.load(full_path).convert_alpha()
    frames.append(surf)

# ---------------------------
# scheletons images
# ---------------------------

scheleton_frames = []
bat_folder = path.join('resources', 'skeleton')
for file_name in listdir(bat_folder):
    full_path = path.join(bat_folder, file_name)
    surf = pygame.image.load(full_path).convert_alpha()
    scheleton_frames.append(surf)