import sys, os
import numpy as np

from src.core.python_source.game_manager import GameManager


if __name__ == "__main__":

    dir_path = os.path.dirname(os.path.realpath(__file__))
    project_path = os.path.split(dir_path)[0]

    cpp_update_state_code = os.path.join(project_path, 'src/core/cpp_build/UpdateState')
    sys.path.insert(0, cpp_update_state_code)

    import state_manager_omp

    game_name = 'game_name'
    path_to_game_folder = os.path.join(project_path, 'data')
    time_points = 10

    # initialize the state manager written in cpp:
    sm_cpp = state_manager_omp.StateManager()

    print "\nv: Path and game name are not initialized: "
    print "path: " + sm_cpp.path_to_game_folder
    print "name: " + sm_cpp.game_name

    # initialise the path and the game name:
    sm_cpp.path_to_game_folder = path_to_game_folder
    sm_cpp.game_name = game_name
    print "\nv: Path and game name are now initialized to the data folder in the project: "
    print "path: " + sm_cpp.path_to_game_folder
    print "name: " + sm_cpp.game_name

    # produce a seed with the python state manager:
    sm_py = GameManager(path_to_game_folder=path_to_game_folder, game_name=game_name)
    sm_py.erase_the_game(erase_seed=True, safe_erase=False)
    sm_py.max_update_time = time_points

    m_0 = np.zeros([7, 7], dtype=np.uint8)
    m_0[2,2], m_0[3, 3], m_0[4, 1], m_0[4, 2], m_0[4, 3] = [1] * 5

    sm_py.saver(m_0, 0)

    # update one step the seed with cpp:
    for t in range(time_points):
        sm_cpp.update_state_once(t)

    # finally see the game:
    sm_py.see_the_game()
