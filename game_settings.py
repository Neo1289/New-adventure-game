import pygame
from os.path import join
from os import walk
from os import *
import sys
from pytmx.util_pygame import load_pygame
from random import randint
pygame.init()
import time

screen_width = 1024
screen_height = 768

WINDOW_WIDTH, WINDOW_HEIGHT = screen_width, screen_height -50
TILE_SIZE = 32

button_color = (255, 255, 255)
FONT_SIZE = 20

####player features blit it resuses the same color as the button question
caption = "Blit Example - Bottom Right"
font_caption = pygame.font.SysFont('Georgia', 20)
text_surface = font_caption.render(caption, True, button_color)
padding = 30
text_rect = text_surface.get_rect()
text_rect.bottomright = (WINDOW_WIDTH - padding, WINDOW_HEIGHT - padding)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

####MAPS
maps = {}
for dirpath, dirnames, filenames in walk(path.join('resources', 'world')):
    for filename in filenames:
        if filename.lower().endswith('.tmx'):
            maps[(filename.split('.')[0])] = (load_pygame(path.join('resources','world',filename)))

