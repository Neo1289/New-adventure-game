import pygame
from main_program import Game
from ToolBar import ToolBar

STATE_ONE = "state_one"
STATE_TWO = "state_two"
current_state = STATE_ONE

def state_manager(current_state):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        current_state = STATE_TWO
    elif keys[pygame.K_RETURN]:
        current_state = STATE_ONE
    return current_state

def state_looper(current_state):

    if current_state == STATE_ONE:
        main_game = Game()
        main_game.setup()
        main_game.mapping()
        main_game.run()
    elif current_state == STATE_TWO:
        tool_bar = ToolBar()
        tool_bar.run()

if __name__ == '__main__':
  state_looper(current_state)
