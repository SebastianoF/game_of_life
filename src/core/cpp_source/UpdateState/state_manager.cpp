/*
Update state basic: same implementation of the game of life, as the python
update_state_manager, with internal load and save methods (no state_manager)

It is a stand alone implementation, callable by python that must provide a complete implementation
of the game of life.

Tests are provided in the Python embedding, and performed with nosetests. 
*/

#include <string>
#include <sstream>
#include <cstdlib>
#include <stdlib.h>
#include <iostream>
#include <Eigen/Dense>

#include <fstream>

class StateManager
{
    private:
        std::string m_path_to_game_folder;
        std::string m_game_name;

    public:

        // constructors:
        StateManager() {
            m_path_to_game_folder = "set the path";
            m_game_name = "set the name game";
        }

        // getter and setter:
        std::string get_path_to_game_folder() {
            return m_path_to_game_folder;
        }

        void set_path_to_game_folder(std::string new_path_to_game_folder) {
            m_path_to_game_folder = new_path_to_game_folder;
        }

        std::string get_game_name() {
            return m_game_name;
        }

        void set_game_name(std::string new_game_name) {
            m_game_name = new_game_name;
        }

        //update state: 

        void update_state(int i) {
            Eigen::MatrixXd m(2,2);
            m(0,0) = i;
            m(1,0) = 2.5;
            m(0,1) = -1;
            m(1,1) = m(1,0) + m(0,1);
            std::cout << m << std::endl;
        }
};



#include <boost/python.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(state_manager)
{
    class_<StateManager>("StateManager", init<>())
        .add_property("path_to_game_folder", &StateManager::get_path_to_game_folder, &StateManager::set_path_to_game_folder)
        .add_property("game_name", &StateManager::get_game_name, &StateManager::set_game_name)
        .def("update_state", &StateManager::update_state)
        ;

}







