cmake_minimum_required(VERSION 2.8.3)

set(PROJECT_NAME "game_of_life")
project(${PROJECT_NAME})

# Make sure Git is available.

find_package(Git REQUIRED)
if (WIN32)
  set(GITCOMMAND ${GIT_EXECUTABLE})
endif()

# Find Eigen

#FIND_PACKAGE(Eigen REQUIRED)
#INCLUDE_DIRECTORIES(${Eigen_INCLUDE_DIR})
#MESSAGE("Loading Eigen from ${Eigen_INCLUDE_DIR}")

set(Eigen_INCLUDE_DIRS /Users/sebastiano/sw_libraries/eigen-lib/cmake/FindEigen3.cmake)
include_directories(${Eigen_INCLUDE_DIRS})


# Setup boost

FIND_PACKAGE(PythonInterp)
FIND_PACKAGE(PythonLibs)
FIND_PACKAGE(Boost COMPONENTS python)

ENABLE_TESTING()
INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})
LINK_LIBRARIES(${Boost_LIBRARIES} ${PYTHON_LIBRARIES})


# Add subdirectories

ADD_SUBDIRECTORY(HelloWorld)
ADD_SUBDIRECTORY(HelloBox)
ADD_SUBDIRECTORY(UpdateState)
