import sys, os, time
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


if __name__ == "__main__":

    # Path settings - compatible with stats methods.

    dir_path = os.path.dirname(os.path.realpath(__file__))
    project_path = os.path.split(dir_path)[0]
    path_to_game_folder = os.path.join(project_path, 'data')
    path_to_saved_data = os.path.join(path_to_game_folder, 'data_increasing_board2.npy')

    print "Data acquired from:"
    print path_to_game_folder + "\n"

    data = np.load(path_to_saved_data)

    mean_data = np.mean(data, axis=2)
    std_data = np.std(data, axis=2)

    print mean_data.shape
    print std_data.shape

    print mean_data

    number_of_board_dim = mean_data.shape[0]

    fig = plt.figure(1, figsize=(7, 5), dpi=100)
    fig.subplots_adjust(left=0.15, right=0.9, bottom=0.2, top=0.85)
    ax  = fig.add_subplot(111)

    ax.errorbar(range(number_of_board_dim), mean_data[:, 0], yerr=std_data[:, 0], fmt='-o', color='b', label="python")
    ax.errorbar(range(number_of_board_dim), mean_data[:, 1], yerr=std_data[:, 1], fmt='-o', color='g', label="serial C++")
    ax.errorbar(range(number_of_board_dim), mean_data[:, 2], yerr=std_data[:, 2], fmt='-o', color='r', label="parallel C++")
    ax.set_title('Computational time versus board dimension')
    ax.set_xlabel('board dimension (cells)')
    ax.set_ylabel('computational time (sec)')
    shape_dimensions = [(i, j) for i, j in zip(range(10, 86, 5), range(10, 86, 5))]

    my_xticks = [str(i) + 'x' + str(j) for i, j in shape_dimensions]
    plt.xticks(range(number_of_board_dim), my_xticks, rotation=45)

    ax.legend(loc=2)
    # time of the loader will be included and it is different for the python case and the c++ case.
    # This may be one of the reasons why cython should be used before Boost::Eigen.

    plt.show()
