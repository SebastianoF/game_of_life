import numpy as np
import os

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from src.core.python_source.game_manager import GameManager


project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
path_to_game_folder = os.path.join(project_path, 'data')

game_name = 'r_game_1'
time_points = 400

usm = GameManager(path_to_game_folder, game_name, time_points)
usm.generate_game(x_dim=50, y_dim=50, regenerate_seed=True)


fig = plt.figure(1, figsize=(7, 7), dpi=100)
fig.subplots_adjust(left=0.04, right=0.98, top=0.92, bottom=0.08)
ax  = fig.add_subplot(111)
plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)

ims = []
for k in range(time_points+1):
    st = usm.loader(k)
    im = plt.imshow(st, cmap='Greys', interpolation='nearest', animated=True)
    ims.append([im])


#print ims

im_ani = animation.ArtistAnimation(fig, ims, interval=100, repeat_delay=3000, blit=False)

plt.show()