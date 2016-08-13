import os
import numpy as np

from src.core.python_source.game_manager import GameManager


if __name__ == "__main__":

    project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path_to_game_folder = os.path.join(project_path, 'data')

    game_name = 'gun_'
    time_points = 70

    # open an instance of a Game manager
    usm = GameManager(path_to_game_folder, game_name, time_points)

    # create and save the seed (state at time state 0) in the specified folder:
    m_0 = np.zeros([50, 30], dtype=np.uint8)

    m_0[1, 5] = 1
    m_0[1, 6] = 1
    m_0[2, 5] = 1
    m_0[2, 6] = 1
    m_0[11, 5] = 1
    m_0[11, 6] = 1
    m_0[11, 7] = 1
    m_0[12, 4] = 1
    m_0[12, 8] = 1
    m_0[13, 3] = 1
    m_0[13, 9] = 1
    m_0[14, 3] = 1
    m_0[14, 9] = 1
    m_0[15, 6] = 1
    m_0[16, 4] = 1
    m_0[16, 8] = 1
    m_0[17, 5] = 1
    m_0[17, 6] = 1
    m_0[17, 7] = 1
    m_0[18, 6] = 1
    m_0[21, 3] = 1
    m_0[21, 4] = 1
    m_0[21, 5] = 1
    m_0[22, 3] = 1
    m_0[22, 4] = 1
    m_0[22, 5] = 1
    m_0[23, 2] = 1
    m_0[23, 6] = 1
    m_0[25, 1] = 1
    m_0[25, 2] = 1
    m_0[25, 6] = 1
    m_0[25, 7] = 1
    m_0[35, 3] = 1
    m_0[35, 4] = 1
    m_0[36, 3] = 1
    m_0[36, 4] = 1
    m_0[35, 22] = 1
    m_0[35, 23] = 1
    m_0[35, 25] = 1
    m_0[36, 22] = 1
    m_0[36, 23] = 1
    m_0[36, 25] = 1
    m_0[36, 26] = 1
    m_0[36, 27] = 1
    m_0[37, 28] = 1
    m_0[38, 22] = 1
    m_0[38, 23] = 1
    m_0[38, 25] = 1
    m_0[38, 26] = 1
    m_0[38, 27] = 1
    m_0[39, 23] = 1
    m_0[39, 25] = 1
    m_0[40, 23] = 1
    m_0[40, 25] = 1
    m_0[41, 24] = 1

    usm.saver(m_0, time_state=0)  # the seed, state at time state 0, is saved in the folder specified

    # generate the game in the game folder specified:
    usm.generate_the_game()

    usm.see_the_game(save=True)

    # clean the data folder and the saved movie:
    usm.erase_the_game(erase_seed=True, safe_erase=False, erase_movie=False)
