#brew install clang-omp
# run with CC=clang-omp CXX=clang-omp++ cmake ../cpp_source/
# than make

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

# Add openmp

find_package(OpenMP)
if (OPENMP_FOUND)
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
endif()


# Add subdirectories

ADD_SUBDIRECTORY(HelloWorld)
ADD_SUBDIRECTORY(HelloWorldOMP)
ADD_SUBDIRECTORY(HelloBox)
ADD_SUBDIRECTORY(UpdateState)
