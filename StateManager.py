# state_manager.py
class StateManager:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, name, state):
        self.states[name] = state

    def set_state(self, name):
        self.current_state = self.states.get(name)

    def run_current_state(self):
        if self.current_state:
            if self.current_state.__class__.__name__ == 'Game':
                self.current_state.run_main_state()
            else:
                self.current_state.run()
