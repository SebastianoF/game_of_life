import sys, os
import numpy as np

from numpy.testing import assert_array_equal

from src.core.python_source.game_manager import GameManager

dir_path = os.path.dirname(os.path.realpath(__file__))
project_path = os.path.split(dir_path)[0]

cpp_update_state_code = os.path.join(project_path, 'src/core/cpp_build/UpdateState')
sys.path.insert(0, cpp_update_state_code)

import state_manager
import state_manager_omp


test_folder = os.path.dirname(os.path.realpath(__file__))
data_test_folder = os.path.join(test_folder, 'data_test')
game_name = 'test_block'

def test_still_life_block_in_1_time_step_cpp():

    # python game manager:
    usm = GameManager(data_test_folder, game_name, 2)

    sm_cpp = state_manager.StateManager()
    sm_cpp.path_to_game_folder = data_test_folder
    sm_cpp.game_name = game_name

    # create and save the artificial seed:
    m_0 = np.zeros([4,4], dtype=np.uint8)
    m_0[1,2], m_0[2,1], m_0[2, 2] = [1, 1, 1]
    usm.saver(m_0, 0)

    sm_cpp.update_state_once(0)
    sm_cpp.update_state_once(1)
    # check that after 2 iteration the seed is the block
    m_test = m_0[:]; m_test[1,1] = 1
    m_2 = usm.loader(1)
    assert_array_equal(m_2, m_test)

    # clean the game from data:
    usm.erase_the_game(erase_seed=False, safe_erase=False)


def test_still_life_block_in_1_time_step_cpp_omp():
    # python game manager:
    usm = GameManager(data_test_folder, game_name, 2)

    sm_cpp = state_manager_omp.StateManagerOMP()
    sm_cpp.path_to_game_folder = data_test_folder
    sm_cpp.game_name = game_name

    # create and save the artificial seed:
    m_0 = np.zeros([4,4], dtype=np.uint8)
    m_0[1,2], m_0[2,1], m_0[2, 2] = [1, 1, 1]
    usm.saver(m_0, 0)

    sm_cpp.update_state_once(0)
    sm_cpp.update_state_once(1)
    # check that after 2 iteration the seed is the block
    m_test = m_0[:]; m_test[1,1] = 1
    m_2 = usm.loader(1)
    assert_array_equal(m_2, m_test)

    # clean the game from data:
    usm.erase_the_game(erase_seed=False, safe_erase=False)
