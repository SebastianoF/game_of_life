import os
import numpy as np

from numpy.testing import assert_array_almost_equal, assert_array_equal
from nose.tools import assert_equal, assert_raises

from src.core.python_source.game_manager import GameManager


test_folder = os.path.dirname(os.path.realpath(__file__))
data_test_folder = os.path.join(test_folder, 'data_test')


def test_still_life_block_in_1_time_step():

    usm = GameManager(data_test_folder, 'test_block', 2)

    # create and save the artificial seed:
    m_0 = np.zeros([4,4], dtype=np.uint8)
    m_0[1,2], m_0[2,1], m_0[2, 2] = [1, 1, 1]
    usm.saver(m_0, 0)

    # generate the game
    usm.generate_game()

    # check that after 2 iteration the seed is the block
    m_test = m_0[:]; m_test[1,1] = 1
    m_2 = usm.loader(2)
    assert_array_equal(m_2, m_test)

    # video here!

    # clean after yourself:
    usm.erase_the_game(erase_seed=False, safe_erase=False)


def test_gosper_glider_gun():

    usm = GameManager(data_test_folder, 'glider_gun', 2)

    # create and save the artificial seed:
    m_0 = np.zeros([50,50], dtype=np.uint8)
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

    usm.saver(m_0, 0)

    # generate the game
    usm.generate_game()

    # check that after 2 iteration the seed is the block
    m_test = m_0[:]; m_test[1,1] = 1
    m_2 = usm.loader(2)
    assert_array_equal(m_2, m_test)

    # video here!

    # clean after yourself:
    usm.erase_the_game(erase_seed=False, safe_erase=False)


test_still_life_block_in_1_time_step()