import numpy as np
import os

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class StateManager(object):
    """
    Interface for the state of a game. To reduce computational costs, and in particular to have the method to update a
    state disentangled by any structure that may add a confunding factor in the computational time analysis, there is
    no class for the object state, being a .txt, and there is no class for the object game, being a set of indexed
    .txt files.
    """

    def __init__(self, path_to_game_folder, game_name):

        self.path_to_game_folder = path_to_game_folder
        self.game_name = game_name

        self.seed_name = str(self.game_name) + '_t0' + '.txt'
        self.path_to_seed = os.path.join(path_to_game_folder, self.seed_name)

    def loader(self, time_state):
        """
        from a State Manager and the time_state to the state as a numpy nd.array.
        :param time_state:
        :return:
        """
        filename = os.path.join(self.path_to_game_folder, self.game_name + '_t' + str(time_state) + '.txt')
        arr = np.loadtxt(filename)
        arr.astype(np.uint8)
        return arr  # the np.ndarray

    def saver(self, input_array_state, time_state):
        """
        From an input state, stored into a np.ndarray it creates a  state into a txt file in the game_folder
        with the name game_name
        :param input_array_state: np.ndarray where the state information is stored
        :param time_state: time of the input state
        :return: creates the xxx_tyyy.txt state with content the input_state as np.ndarray and
        with xxx=game_name and yyy as time_state
        """
        ''' # commented to spare time:
        if not input_array_state.ndim == 2:
            raise IOError('Input state must be 2-dimensional.')
        if not input_array_state.dtype == np.uint8:
            raise IOError('Type of the input array must be uint8 - usinged integer 8 bit.')
        if not set(input_array_state.reshape(np.prod(input_array_state.shape)).tolist()) == {0, 1}:
            raise IOError('Input array must be binary.')
        '''
        filename = os.path.join(self.path_to_game_folder, self.game_name + '_t' + str(time_state) + '.txt')
        np.savetxt(filename, input_array_state, fmt='%1u')

    def initialise_random(self, dim_x, dim_y, ones_percentage=1./10):
        """

        :param dim_x: x dimension of the matrix
        :param dim_y: y dimension of the matrix
        :param path_to_game: path to the folder where the game is saved
        :param game_name: name of the game
        :param ones_percentage: percentage of ones in the state.
        :return: save a random initial state of a game
        """
        st = np.random.choice([0, 1], size=(dim_x, dim_y), p=[1 - ones_percentage, ones_percentage])
        st = st.astype(np.uint8)
        print('Random state generated.')
        self.saver(st, time_state=0)

    def see_the_state(self, time_state):
        """
        see the state at the given time point
        :param time_state: given time point.
        :return:
        """

        fig = plt.figure(1, figsize=(7, 7), dpi=100)
        fig.subplots_adjust(left=0.04, right=0.98, top=0.92, bottom=0.08)
        ax  = fig.add_subplot(111)

        pic = ax.imshow(self.loader(time_state=time_state), cmap='Greys', interpolation='nearest')

        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)

        #plt.colorbar(aa, orientation='vertical')  # yes indeed, black are 1, white are zeros

        plt.show()