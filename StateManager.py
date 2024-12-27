from main_program import Game
from test import main_game_loop

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
            self.current_state.run()

if __name__ == '__main__':
    state_manager = StateManager()
    # ---------------------------
    # starting main game
    # ---------------------------
    main_game = Game()
    main_game.setup()
    main_game.mapping()
    # ---------------------------
    # adding main game state
    # ---------------------------
    state_manager.add_state('main_game', main_game)
    # ---------------------------
    # Set the initial state to the game
    # ---------------------------
    state_manager.set_state('main_game')
    # ---------------------------
    # Run the current state
    # ---------------------------
    state_manager.run_current_state()
