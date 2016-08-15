/*
Update state basic: same implementation of the game of life, as the python
update_state_manager, with internal load and save methods (no state_manager)

It is a stand alone implementation, callable by python that must provide a complete implementation
of the game of life.

Tests are provided in the Python embedding, and performed with nosetests. 
*/

#include <string>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <stdlib.h>
#include <iostream>
#include <Eigen/Dense>

#include <omp.h>

#define MAXBUFSIZE  ((int) 1e6)


// auxiliary functions:

int positive_modulo(int i, int n) {
    return (i % n + n) % n;
}

int cell_degree(int i, int j, int x_dim, int y_dim, Eigen::MatrixXi state_arr) {
    
    int a = 0;

    for (int x=-1; x<=1; x++){
        for (int y=-1; y<=1; y++) {
            if ( x != 0 || y != 0 ) {
                a = a + state_arr(positive_modulo(x+i,x_dim), positive_modulo(y+j,y_dim));
            }
        }
    }
    return a;
}



class StateManager
{
    private:
        std::string m_path_to_game_folder;
        std::string m_game_name;

    public:

        // constructors:

        StateManager() {
            m_path_to_game_folder = "Path not defined.";
            m_game_name = "Game name not defined.";
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

        // load state:

        Eigen::MatrixXi loader(int in_time) {
            int cols = 0, rows = 0;
            double buff[MAXBUFSIZE];

            std::string state_path;
            state_path =  m_path_to_game_folder + "/" + m_game_name + "_t" +  std::to_string(in_time) + ".txt";
            
            std::ifstream in_file;
            in_file.open(state_path);

            while (! in_file.eof())
                {
                std::string in_line;
                getline(in_file, in_line);

                int tmp_cols = 0;
                std::stringstream stream(in_line);
                while(! stream.eof())
                    stream >> buff[cols*rows + tmp_cols++];

                if (tmp_cols == 0)
                    continue;

                if (cols == 0)
                    cols = tmp_cols;

                rows++;
                }

            in_file.close();
            rows--;

            Eigen::MatrixXi result(rows, cols);
            for (int i = 0; i < rows; i++)
                for (int j = 0; j < cols; j++)
                    result(i,j) = buff[cols * i + j];
            return result;
        }
        
        // save state:

        void saver(Eigen::MatrixXi state_arr, int in_time) {

            std::string state_path;
            state_path =  m_path_to_game_folder + "/" + m_game_name + "_t" +  std::to_string(in_time) + ".txt";

            std::ofstream file(state_path.c_str());
            if (file.is_open()) {
                file << state_arr << "\n";
            }
            file.close();
        }

        // update state from array - very naife parallelisation: 

        Eigen::MatrixXi update_from_array(Eigen::MatrixXi state_arr) {
            
            int x_dim = state_arr.rows(), 
                y_dim = state_arr.cols();

            Eigen::MatrixXi deg_arr = Eigen::MatrixXi::Zero(x_dim, y_dim);
            Eigen::MatrixXi new_state_arr = Eigen::MatrixXi::Zero(x_dim, y_dim);

            #pragma omp parallel for
            for(int i=0; i < x_dim; i++) {
                for(int j=0; j < y_dim; j++){
                    deg_arr(i, j) = cell_degree(i, j, x_dim, y_dim, state_arr);
                }
            }
            #pragma omp parallel for
            for(int i = 0; i<x_dim; i++) {
                for(int j = 0; j<y_dim; j++){
                    if (state_arr(i, j) == 1 && deg_arr(i, j) >= 2 && deg_arr(i, j) <= 3) // cell is alive and survives
                        new_state_arr(i, j) = 1;
                    if (state_arr(i, j) == 0 && deg_arr(i, j) == 3) // cell is dead and is the beloved of other 3 cells
                        new_state_arr(i, j) = 1;
                }
            }

            return new_state_arr;
        }

        // update state once:

        void update_state_once(int in_time) {
            
            Eigen::MatrixXi input_state;
            Eigen::MatrixXi new_state;

            // load state
            input_state = loader(in_time);

            // update from array
            new_state = update_from_array(input_state);

            //save
            saver(new_state, in_time + 1);

        }
};



#include <boost/python.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(state_manager_omp)
{
    class_<StateManager>("StateManager", init<>())
        .add_property("path_to_game_folder", &StateManager::get_path_to_game_folder, &StateManager::set_path_to_game_folder)
        .add_property("game_name", &StateManager::get_game_name, &StateManager::set_game_name)
        .def("update_state_once", &StateManager::update_state_once)
        .def("update_from_array", &StateManager::update_from_array)
        .def("loader", &StateManager::loader)
        .def("saver", &StateManager::saver)
        ;

}
