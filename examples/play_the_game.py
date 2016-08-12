import os
from src.core.python_source.game_manager import GameManager


if __name__ == "__main__":

    project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path_to_game_folder = os.path.join(project_path, 'data')
    game_name='random_game'

    usm = GameManager(path_to_game_folder=path_to_game_folder,
                             game_name='random_game_1')

    # produce a small game 50x50 with 10 time points
    usm.max_update_time = 10
    usm.generate_game(x_dim=20, y_dim=20)