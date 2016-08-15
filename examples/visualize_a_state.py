import os

from src.core.python_source.state_manager import StateManager


if __name__ == "__main__":

    # Setting path and name of the game:
    project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path_to_game_folder = os.path.join(project_path, 'data')
    game_name='random_game'

    # initialize the state using an instance of the state manager:
    sm = StateManager(path_to_game_folder=path_to_game_folder, game_name=game_name)
    sm.initialise_random(10, 10)

    # see the initialized random state:
    sm.see_the_state(0)
