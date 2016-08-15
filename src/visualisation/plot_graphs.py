import sys, os, time
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


if __name__ == "__main__":

    # Path settings - compatible with stats methods.

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    project_path = os.path.split(dir_path)[0]
    path_to_game_folder = os.path.join(project_path, 'data')
    path_to_saved_data = os.path.join(path_to_game_folder, 'data_increasing_board.npy')

    print "Data acquired from:"
    print path_to_game_folder + "\n"

    data = np.load(path_to_saved_data)

    mean_data = np.mean(data, axis=2)
    std_data = np.std(data, axis=2)

    print mean_data.shape
    print std_data.shape

    number_of_board_dim = mean_data.shape[0]

    fig = plt.figure(1, figsize=(7, 7), dpi=100)
    #fig.subplots_adjust(left=0.1, right=0.1, top=0.1, bottom=0.1)
    ax  = fig.add_subplot(111)

    ax.errorbar(range(number_of_board_dim), mean_data[:, 0], yerr=std_data[:, 0], fmt='-o', color='b')
    ax.errorbar(range(number_of_board_dim), mean_data[:, 1], yerr=std_data[:, 1], fmt='-o', color='g')
    ax.set_title('zzz')
    # time of the loader will be included and it is different for the python case and the c++ case.
    # This may be one of the reasons why cython should be used before Boost::Eigen.

    plt.show()
