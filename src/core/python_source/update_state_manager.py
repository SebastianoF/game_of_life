import numpy as np
import os

from src.utils.state_manager import StateManager
from src.utils.aux_functions import cell_degree


class UpdateStateManager(StateManager):
    """
    Core class of the code, python implementation that updates the state.
    Update state once:
        Load the state
        Generate the degree matrix
        Update from the degree matrix to the new state
        Delete the degree matrix to save space before the garbage collector
        Save the new state

    """

    def __init__(self, path_to_game_folder, game_name, max_update_time=100, border_strategy=0):

        super(UpdateStateManager, self).__init__(path_to_game_folder, game_name)

        # periodic boundary condition for the moment
        #self.border_strategy = border_strategy  # 'zeros' if 0, 'snake' if 1

        self.max_update_time = 100
        self.death_threshold = 1     # <= 1 the cell dies
        self.lazzarus_threshold = 4  # >= 4 the cell goes back to life

        self.path_to_seed = os.path.join(path_to_game_folder, self.game_name + '_t0' + '.txt')

    def update_state_once(self, time_state):
        """
        Update the state from state_time to state_time + 1
        :param time_state:
        :return: generate the next state in the game.
        """
        state_arr = self.loader(time_state=time_state)

        deg_arr = np.zeros_like(state_arr)
        x_dim, y_dim = deg_arr.shape
        for i in xrange(x_dim):
            for j in xrange(y_dim):

                deg_arr[i, j] = cell_degree(i, j, x_dim, y_dim, state_arr)

        new_state_arr = np.zeros_like(state_arr)

        for i in xrange(x_dim):
            for j in xrange(y_dim):
                if self.death_threshold < deg_arr[i, j] < self.lazzarus_threshold and state_arr[i,j]:
                    new_state_arr[i, j] = 1
                elif deg_arr[i, j] > self.lazzarus_threshold:
                    new_state_arr[i, j] = 1

        deg_arr = None
        state_arr = None

        self.saver(new_state_arr, time_state=time_state + 1)


    def generate_game(self):

        # check if self.path_to_seed is a file! if not specify that the seed must be provided!
        # tell that you can generate it random with initialise_random.
        pass


