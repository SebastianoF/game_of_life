import os
import numpy as np

from src.core.python_source.game_manager import GameManager


if __name__ == "__main__":

    project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path_to_game_folder = os.path.join(project_path, 'data')

    game_name = 'glider_'
    time_points = 200

    # open an instance of a Game manager
    usm = GameManager(path_to_game_folder, game_name, time_points)

    # create and save the seed (state at time state 0) in the specified folder:
    m_0 = np.zeros([20, 20], dtype=np.uint8)
    m_0[2,2], m_0[3, 3], m_0[4, 1], m_0[4, 2], m_0[4, 3] = [1] * 5
    usm.saver(m_0, time_state=0)  # the seed, state at time state 0, is saved in the folder specified

    # generate the game in the game folder specified:
    usm.generate_the_game()

    usm.see_the_game(save=False)

    # clean the data folder:
    usm.erase_the_game(erase_seed=True, safe_erase=False)
