from main_program import Game
from test import main_game_loop
from game_settings import pygame

class StateManager:
    def __init__(self):
        self.states = {}
        self.current_state = None
        self.running = True

    def add_state(self, name, state):
        self.states[name] = state

    def set_state(self, name):
        self.current_state = self.states.get(name)

    def run_current_state(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    self.add_state('menu', main_game_loop())
                    self.set_state('menu')

            self.current_state.run()
            print(self.current_state)

if __name__ == '__main__':
    state_manager = StateManager()
    main_game = Game()
    state_manager.add_state('main_game', main_game)
    state_manager.set_state('main_game')
    main_game.setup()
    main_game.mapping()
    state_manager.run_current_state()
