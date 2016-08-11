from matplotlib import pyplot as plt
import numpy as np
import os
from os.path import join

from src.state_manager.state_manager import StateManager

# random grid state:
#st = np.random.randn(80, 80)

# initialize the state:
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
path_to_game_folder = join(project_path, 'data')
game_name='random_game'

sm = StateManager(path_to_game_folder=path_to_game_folder, game_name=game_name)

sm.initialise_random(100, 100)

# load the initialized state:
st = sm.loader(time_state=0)

fig = plt.figure(1, figsize=(7, 7), dpi=100)

fig.subplots_adjust(left=0.04, right=0.98, top=0.92, bottom=0.08)

ax  = fig.add_subplot(111)


aa = ax.imshow(st, cmap='Greys', interpolation='nearest')

plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)

#plt.colorbar(aa, orientation='horizontal')

plt.show()
