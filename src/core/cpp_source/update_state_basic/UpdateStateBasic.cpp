/*
Update state basic: same implementation of the game of life, as the python
update_state_manager, with internal load and save methods (no state_manager)

It is a stand alone implementation, callable by python that must provide a complete implementation
of the game of life.

Tests are provided in the Python embedding, and performed with nosetests. 
*/

#include <string>
#include <sstream>

class GameManager
{
	private:
		std::string path_to_seed;
		int max_num_iteration;
				
    public:
        SomeClass(std::string n) : name(n), mNumber(0.0) {}

        std::string name;

        double getNumber() const { return mNumber; }

        void setNumber(double n)
        {
            if (n>3.141592654)
                n = -1;
            mNumber = n;
        }

    private:
        double mNumber;
};


#include <boost/python.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(member)
{
    class_<GameManager>("SomeClass", init<std::string>())
        .def_readwrite("name", & SomeClass::name)
        .add_property("number", &SomeClass::getNumber, &SomeClass::setNumber)
    ;

}




class Rectangle {
    int width, height;
  public:
    void set_values (int,int);
    int area() {return width*height;}
};

void Rectangle::set_values (int x, int y) {
  width = x;
  height = y;
}





