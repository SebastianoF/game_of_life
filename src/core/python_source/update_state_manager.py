import numpy as np


class UpdateStateManager(object):
    """
    Core class of the code, python implementation of the update of the state.
    """

    def __init__(self, path_to_seed, max_update_time=100, border_strategy='zeros'):

        self.path_to_seed = path_to_seed
        self.border_strategy = border_strategy  # 'snake', 'klein', 'moebius'
        self.max_update_time = 100

        self.death_threshold = 1     # <= 1 the cell dies
        self.lazzarus_threshold = 4  # >= 4 the cell goes back to life

    def update_state_once(self, in_state_path):
        # core method: this will be implemented in several ways and will include the parallelsation
        # output: out_state np.ndarray



        # Creates the degree matrix


        # Update from the degree matrix to the new state


        pass

    def generate_game(self):
        pass
