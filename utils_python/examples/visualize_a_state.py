from matplotlib import pyplot as plt
import numpy as np
import os
from os.path import join

from core.state_manager import state_initializer_random, state_loader

# random grid state:
#st = np.random.randn(80, 80)

# initialize the state:
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
path_to_state_folder = join(project_path, 'data')
game_name='random_game'

state_initializer_random(100, 100, path_to_state_folder, game_name=game_name, ones_percentage=1./100)

# load the initialized state:
st = np.loadtxt(join(path_to_state_folder, game_name + '_t0'))

fig = plt.figure(1, figsize=(7, 7), dpi=100)

fig.subplots_adjust(left=0.04, right=0.98, top=0.92, bottom=0.08)

ax  = fig.add_subplot(111)


aa = ax.imshow(st, cmap='Greys', interpolation='none')

plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)

#plt.colorbar(aa, orientation='horizontal')

plt.show()
