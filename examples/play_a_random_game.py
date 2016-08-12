import os

from src.core.python_source.game_manager import GameManager


if __name__ == "__main__":

    project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path_to_game_folder = os.path.join(project_path, 'data')

    game_name = 'r_game_1'
    time_points = 10

    usm = GameManager(path_to_game_folder, game_name, time_points)

    usm.erase_the_game(safe_erase=False, erase_seed=True)
    usm.generate_the_game(x_dim=50, y_dim=50, regenerate_seed=True)

    usm.see_the_game(save=True)