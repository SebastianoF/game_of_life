import os
import numpy as np

from numpy.testing import assert_array_equal

from src.core.python_source.game_manager import GameManager


test_folder = os.path.dirname(os.path.realpath(__file__))
data_test_folder = os.path.join(test_folder, 'data_test')


def test_still_life_block_in_1_time_step():

    usm = GameManager(data_test_folder, 'test_block', 3)

    # create and save the artificial seed:
    m_0 = np.zeros([4,4], dtype=np.uint8)
    m_0[1,2], m_0[2,1], m_0[2, 2] = [1, 1, 1]
    usm.saver(m_0, 0)

    # generate the game
    usm.generate_the_game()

    # check that after 2 iteration the seed is the block
    m_test = m_0[:]; m_test[1,1] = 1
    m_2 = usm.loader(2)
    assert_array_equal(m_2, m_test)

    # clean the game from data:
    usm.erase_the_game(erase_seed=False, safe_erase=False)


def test_oscillating_bar():

    usm = GameManager(data_test_folder, 'oscillating_bar', 3)

    # create and save the artificial seed:
    m_0 = np.zeros([5, 5], dtype=np.uint8)
    m_0[1:4, 2] = [1, 1, 1]

    usm.saver(m_0, 0)
    usm.see_the_state(0)

    # generate the game
    usm.generate_the_game()

    test1 = np.zeros([5, 5], dtype=np.uint8); test1[2, 1:4] = [1, 1, 1]
    test2 = np.zeros([5, 5], dtype=np.uint8); test2[1:4, 2] = [1, 1, 1]

    m_1 = usm.loader(1)
    m_2 = usm.loader(2)

    assert_array_equal(m_1, test1)
    assert_array_equal(m_2, test2)

    usm.erase_the_game(erase_seed=False, safe_erase=False)
