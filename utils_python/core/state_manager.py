"""
In this implementaiton of game of life, a game is a succession of states related by a deterministic rule.
A state is stored as a .txt binary matrix with name name_game_tXX.txt where XX is the index of the state, an
integer number that represents the time of the space.
"""

import numpy as np
from os.path import join


def state_initializer(input_state, path_to_game, game_name='game'):
    # create a file
    pass


def state_initializer_random(n1, n2, path_to_game, game_name='random_game', ones_percentage=1./10):
    """

    :param n1: x dimension of the matrix
    :param n2: y dimension of the matrix
    :param path_to_game: path to the folder where the game is saved
    :param game_name: name of the game
    :param ones_percentage: percentage of ones in the state.
    :return: save a random initial state of a game
    """
    st = np.random.choice([0, 1], size=(n1, n2), p=[1 - ones_percentage, ones_percentage])
    filename = join(path_to_game, game_name + '_t0')
    np.savetxt(filename, st, fmt='%1u')
    print('Random state generated.')


def state_loader(path_to_game, game_name='random_game', time_state=0):
    pass


def state_saver():
    pass


def update_state(in_state):
    # core method: this will be implemented in several ways and will include the parallelsation
    # output: out_state np.ndarray



    # Creates the degree matrix


    # Update from the degree matrix to the new state


    pass


