#include <string>
#include <sstream>
#include <iostream>
#include <fstream>

class Box
{

    private:
        
        std::string m_box_name;  // m_ for class variable k_ for class constant
        float m_height;  
        float m_length;
        float m_width;

    public:

        std::string path_and_filename;

        // constructors:
        Box() {
            m_box_name = "default box";
            m_height = 1.0;
            m_width = 1.0;
            m_length = 1.0;
        }

        Box(std::string& box_name, float& height, float& width, float& length) {
            m_box_name = box_name;
            m_height = height;
            m_width = width;
            m_length = length;
        }
        
        //Box() : m_box_name("default box"), m_height(1.0), m_width(1.0), m_length(1.0) {}

        // destructors:
        ~Box() {}

        // getters and setters:
        
        std::string get_name() {
            return m_box_name;
        }

        void set_name(std::string box_new_name) {
            m_box_name = box_new_name;
        }

        float get_height() {
            return m_height;
        }

        void set_height(float new_height) {
            m_height = new_height;
        }


        float get_width() {
            return m_width;
        }

        void set_width(float new_width) {
            m_width = new_width;
        }

        float get_length() {
            return m_length;
        }

        void set_length(float new_length) {
            m_length = new_length;
        }
        
        // extra
        float get_surface() {
            return 2 * m_height * m_width + 2 * m_width * m_length + 2 * m_length * m_height;
        }

        float get_volume() {
            return m_height * m_width * m_length;
        }

        // viewer
        std::string get_info() {
            std::string s = "Box size = " + std::to_string(m_height) + " x "
                             +  std::to_string(m_width) + " x "
                             +  std::to_string(m_length) + " \n"
                             + "Volume = " + std::to_string(get_volume()) + "\n"
                             + "Surface = " + std::to_string(get_surface()) + "\n";
            return s;
        }

        // save specs:
        void save_info(){
            std::ofstream file_where_to_save;
            file_where_to_save.open(path_and_filename, std::ios::out | std::ios::app | std::ios::binary);
            file_where_to_save << Box::get_info() ;
            file_where_to_save.close();
        }

};


#include <boost/python.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(hello_box)
{
    class_<Box>("Box", init<>())
        //.def(init<>())
        //.def(init<std::string , float, float, float>())
        //.def("__init__" Box::Box(std::string , float, float, float))
        .def_readwrite("file_path", & Box::path_and_filename)
        .add_property("name", &Box::get_name, &Box::set_name)
        .add_property("height", &Box::get_height, &Box::set_height)
        .add_property("width", &Box::get_width, &Box::set_width)
        .add_property("length", &Box::get_length, &Box::set_length)
        .def("surface", &Box::get_surface)
        .def("volume", &Box::get_volume)
        .def("info", &Box::get_info)
        .def("save_info", &Box::save_info)
        ;

}