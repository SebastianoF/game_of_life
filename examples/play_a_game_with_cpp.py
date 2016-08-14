import sys
import os


if __name__ == "__main__":

    dir_path = os.path.dirname(os.path.realpath(__file__))
    project_path = os.path.split(dir_path)[0]

    cpp_update_state_code = os.path.join(project_path, 'src/core/cpp_build/UpdateState')
    sys.path.insert(0, cpp_update_state_code)

    import state_manager


    sm_cpp = state_manager.StateManager()

    print sm_cpp.path_to_game_folder
    print sm_cpp.game_name

    sm_cpp.update_state(5)

