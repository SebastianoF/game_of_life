import sys, os, time
import numpy as np


from src.core.python_source.game_manager import GameManager  # Python


if __name__ == "__main__":

    #################
    # Path settings #
    #################

    dir_path = os.path.dirname(os.path.realpath(__file__))
    project_path = os.path.split(dir_path)[0]

    cpp_update_state_code = os.path.join(project_path, 'src/core/cpp_build/UpdateState')
    sys.path.insert(0, cpp_update_state_code)

    import state_manager  # cpp
    import state_manager_omp  # cpp openMP

    ##############
    # Parameters #
    ##############

    game_name = 'cpp_game_name'
    path_to_game_folder = os.path.join(project_path, 'data')
    time_points = 30

    shape_dimensions = [(i, j) for i, j in zip(range(10, 86, 5), range(10, 86, 5))]
    core_methods = 3  # python, cpp, cpp openMP for the moment
    num_samples_each_shape = 10

    #########################
    # Output data structure #
    #########################
    # where the computational times are stored:

    time_data = np.zeros([len(shape_dimensions), core_methods, num_samples_each_shape], dtype=np.float32)
    # i,j,k = index board dimension, core methods to play the game available [py, cpp], sample size

    #########################
    # game manager creation #
    #########################

    # create the game managers, one with python, one with the plain version of cpp

    gm_py = GameManager(path_to_game_folder=path_to_game_folder, game_name=game_name)
    gm_py.max_update_time = time_points

    sm_cpp = state_manager.StateManager()
    sm_cpp.path_to_game_folder = path_to_game_folder
    sm_cpp.game_name = game_name

    sm_cpp_omp = state_manager_omp.StateManagerOMP()
    sm_cpp_omp.path_to_game_folder = path_to_game_folder
    sm_cpp_omp.game_name = game_name

    ######################
    # Collect statistics #
    ######################

    for shape_index, (dim_x, dim_y) in enumerate(shape_dimensions):

        print "\nPhase = " + str(shape_index) + " / " + str(len(shape_dimensions))
        print "Play " + str(num_samples_each_shape) + " games of dimension " + str(dim_x) + " x "+ str(dim_y)

        for s in range(num_samples_each_shape):

            # erase the previous game if any:
            gm_py.erase_the_game(erase_seed=True, safe_erase=False, erase_movie=True)

            # generate random seed
            gm_py.generate_the_game(x_dim=dim_x, y_dim=dim_y, regenerate_seed=True)

            for t in range(time_points):

                # compute new state with python
                start_py = time.time()
                new_state_arr_py = gm_py.update_state_once(t)
                time_data[shape_index, 0, s] += (time.time() - start_py)

                # compute new state with cpp
                start_cpp = time.time()
                new_state_arr_cpp = sm_cpp.update_state_once(t)
                time_data[shape_index, 1, s] += (time.time() - start_cpp)

                # compute new state with cpp OMP
                start_cpp = time.time()
                new_state_arr_cpp_omp = sm_cpp_omp.update_state_once(t)
                time_data[shape_index, 2, s] += (time.time() - start_cpp)

    # Erase again for the last game
    gm_py.erase_the_game(erase_seed=True, safe_erase=False, erase_movie=True)

    # Save the matrix in data with reasonable names in numpy format.
    # It will be loaded and elaborated in the visualisation folder.
    path_to_saved_data = os.path.join(path_to_game_folder, 'data_increasing_board.npy')
    np.save(path_to_saved_data, time_data)
    print "\nComputational time comparison to play the game when increasing board shape concluded."
    print "Data saved in " + path_to_saved_data
