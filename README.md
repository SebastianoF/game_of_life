# boost::python-based Conway's game of life implementation

Here is an **IN PROGRESS** possible implementation of the Conway's game of life.
Aim of the code is to compare the performance between different implementation of the code at the core of Game of Life in C++ and python.

Useful links are:
 
+ [Game of life theory, from wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
+ [C++ advanced programming for research, from UCL](http://rits.github-pages.ucl.ac.uk/research-computing-with-cpp/)
+ [Catch.hpp test framework for the C++ code](http://baptiste-wicht.com/posts/2014/07/catch-powerful-yet-simple-cpp-test-framework.html)
+ [Nosetest unit test for the Python code](http://pythontesting.net/framework/nose/nose-introduction/)
+ [Guide to install boost::python] (http://www.pyimagesearch.com/2015/04/27/installing-boost-and-boost-python-on-osx-with-homebrew/)
+ [Tutorial for boost::python from Joel de Guzman](http://www.boost.org/doc/libs/1_46_1/libs/python/doc/tutorial/doc/html/index.html "Boost.Python tutorial").
+ [Really cool additional tutorial for boost::python from github, authored by Alchimh3011](https://github.com/TNG/boost-python-examples)
+ [Alternative implementaiton of game of life with analogous aims and with a very detailed C++ object oriented structure from github, authored by Michael Ebner](https://github.com/renbem/RCCPP-coursework02)


# Prerequisites

### general

+ [CMake](http://www.cmake.org "CMake project page") (>= 2.8.3)
+ [Boost](http://www.boost.org/ "Boost project page") (tested with 1.4.2, but should work with >= 1.3.2)
+ [Python](http://www.python.org "Python home page") (tested with 2.7, but should work with >= 2.2)
+ a C++ compiler for your platform, e.g. [GCC](http://gcc.gnu.org "GCC home") or [MinGW](http://www.mingw.org "Minimalist GNU for Windows")

### Mac OS X with [homebrew](http://brew.sh)

To install with homebrew the package boost python: 

+ `brew install cmake boost-python`

The full path to the the homebrew python lib must be manually provided:

    cmake -DPYTHON_LIBRARY=/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/libpython2.7.dylib ..

# Code structure:

A *state* of an instance of a game is, in this implementation, a binary matrix of given dimension.
A *game* is a set of numbered states, indexed by a parameter called time. The first one is called *seed* while the following are generated according to the rules of game of life from the seed.
Each state is stored in a .txt file named name_of_the_game_txx.txt where xx is the time index.
The python subpackage *src* contains the state manager, whose aim is to create random seeds, load and save states as .txt with the correct name, and additional utils.
The core methods to generate the following state, given an initial one are in the python package  *src/core/*. Here both python and C++ is stored.
The python subpackage *visualisation* contains the method to visualise the generated games stored in the newly created folder *data*. 

 
# How to run (once boost-python is installed)

This code is tested for Python 2.7.11, on a Mac OS X 10.11.5. Python libraries used here are:
sys, os, numpy, matplotlib.


To run the code, create the folder 'data' in the main directory: it will contains all the output generated by the program in the examples.
Under

    /src/core

create the folder cpp_build, then 

    cd /cd/src/core/cpp_build
    ccmake ../cpp_source

in cmake, configure and generate the source code, then quit and

    make

To make sure the code is correctly configured and the c++ code has been wrapped correctly from an ipython terminal type

    run examples/hello_world_cpp_wrap.py

If everything works to play a game of life initialized with a random seed, type

    run examples/play_the_game.py

This command will create a game, as a sequence of numbered states stored in .txt format inside the newly created folder *data*.  


## Documentation

A documentation with the results and the comparisons between the various method is available in the folder *report*.

## :eton lanif A

.yrotisoper cilbup eht ni detats ylraelc si eludom eht ot ecnerefer tcerid on ,srehcaet eht yb deriuqer sA .notgnirehteH semaJ dna noskralC ttaM yb LCU ta thguat ,2000GYHPM ++C htiw gnitupmoc hcraeseR eludom eht gnirud dengissa krowesruoc dnoces eht si sihT
