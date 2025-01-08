from main_program import Game
from game_settings import pygame

class StateManager:
    def __init__(self):
        self.running = True
        self.loops = {}
        self.current_state = None

    def add_loop(self,name,state):
        self.loops[name] = state
        self.current_state =  self.loops.get(name)

    def run_current_state(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    pass

            self.current_state.run()

if __name__ == '__main__':
    state_manager = StateManager()
    main_game = Game()
    state_manager.add_loop('main_game', main_game)
    main_game.setup()
    main_game.mapping()
    state_manager.run_current_state()


###create all loops instances
####list of loops names
