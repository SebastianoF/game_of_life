import os
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def plot_a_sequence_of_images(list_arr):
    """
    :param list_arr: list of 2d arrays of the same dimension
    :return: animation having the sequence of images as input
    """
    fig = plt.figure(1, figsize=(7, 7), dpi=100)
    fig.subplots_adjust(left=0.04, right=0.98, top=0.92, bottom=0.08)
    ax  = fig.add_subplot(111)
    plt.setp(ax.get_xticklabels(), visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)

    ims = []
    for arr in list_arr:
        im = plt.imshow(arr, cmap='Greys', interpolation='nearest', animated=True)
        ims.append([im])

    im_ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=3000, blit=False)

    #plt.show()

    return im_ani