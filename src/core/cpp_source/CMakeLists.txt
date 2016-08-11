cmake_minimum_required(VERSION 2.8.3)

set(PROJECT_NAME "game_of_life")
project(${PROJECT_NAME})

FIND_PACKAGE(Git REQUIRED)

FIND_PACKAGE(PythonInterp)
FIND_PACKAGE(PythonLibs)
FIND_PACKAGE(Boost COMPONENTS python)

ENABLE_TESTING()
INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})
LINK_LIBRARIES(${Boost_LIBRARIES} ${PYTHON_LIBRARIES}) # Deprecated but so convenient!

ADD_SUBDIRECTORY(HelloWorld)

