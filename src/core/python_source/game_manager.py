import numpy as np
import os

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from src.utils.state_manager import StateManager
from src.utils.aux_functions import cell_degree


class GameManager(StateManager):
    """
    Core class of the code, python implementation that updates the state.
    Update state once:
        Load the state
        Generate the degree matrix
        Update from the degree matrix to the new state
        Delete the degree matrix to save space before the garbage collector
        Save the new state

    """

    def __init__(self, path_to_game_folder, game_name, max_update_time=100):

        super(GameManager, self).__init__(path_to_game_folder, game_name)

        # periodic boundary condition for the moment
        #self.border_strategy = border_strategy  # 'zeros' if 0, 'snake' if 1

        self.max_update_time = max_update_time

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
                if state_arr[i, j] == 1 and 2 <= deg_arr[i, j] <= 3:  # cell is alive and survives
                    new_state_arr[i, j] = 1
                if state_arr[i, j] == 0 and deg_arr[i, j] == 3:  # cell is dead and is the beloved of 3
                    new_state_arr[i, j] = 1

        deg_arr, state_arr = None, None

        self.saver(new_state_arr, time_state=time_state + 1)

    def generate_the_game(self, x_dim=200, y_dim=200, ones_percentage=1./10, regenerate_seed=False):

        if not regenerate_seed and not os.path.isfile(self.path_to_seed):
            raise IOError('Game has no seed generated')

        # if there is no seed or you asked to regenerate, then a random seed is generated:
        # seed with the same name will be overwritten
        if regenerate_seed:
            self.initialise_random(x_dim, y_dim, ones_percentage=ones_percentage)

        # update the state until the max update time.
        for t in range(self.max_update_time):
            self.update_state_once(t)

    def erase_the_game(self, erase_seed=True, safe_erase=True):

        if safe_erase:
            if erase_seed:
                sure = raw_input("Are you sure you want to erase the game, including the seed (y/n): ")
            else:
                sure = raw_input("Are you sure you want to erase the game (y/n): ")
        else:
            sure = 'y'

        if sure.lower() == 'n':
            return
        elif sure.lower() == 'y':
            for name_state in os.listdir(self.path_to_game_folder):
                if name_state.startswith(self.game_name):
                    if erase_seed:
                        os.remove(os.path.join(self.path_to_game_folder, name_state))
                    elif not name_state == self.seed_name:
                        os.remove(os.path.join(self.path_to_game_folder, name_state))

            print 'Game in the folder ' + self.path_to_game_folder + ' named ' + self.game_name + ' has been erased.'

        else:
            print 'input not understood, game not erased. Please write y or n next time.'

    def see_the_game(self, save=False):

        fig = plt.figure(1, figsize=(7, 7), dpi=100)
        fig.subplots_adjust(left=0.04, right=0.98, top=0.92, bottom=0.08)
        ax  = fig.add_subplot(111)
        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)

        ims = []
        for k in range(self.max_update_time+1):
            arr = self.loader(k)
            im = plt.imshow(arr, cmap='Greys', interpolation='nearest', animated=True)
            ims.append([im])

        anim = animation.ArtistAnimation(fig, ims, interval=200, repeat_delay=200, blit=False)

        if save:
            # Set up formatting for the movie files
            Writer = animation.writers['ffmpeg']
            writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
            anim.save(self.path_to_seed[-4] + '.mp4', writer=writer)

        plt.show()
