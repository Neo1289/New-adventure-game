import pygame
from os.path import join
from os import walk
from os import *
import sys
from pytmx.util_pygame import load_pygame
from random import randint
pygame.init()
import time

info = pygame.display.Info()
screen_width = 1024
screen_height = 768

WINDOW_WIDTH, WINDOW_HEIGHT = screen_width, screen_height -50
TILE_SIZE = 32

button_color = (255, 255, 255)
FONT_SIZE = 20

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

####MAPS

world_map = load_pygame(join('resources', 'world', 'world_map.tmx'))
map_manor = load_pygame(join('resources', 'world', 'manor.tmx'))
