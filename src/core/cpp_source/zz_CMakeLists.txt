cmake_minimum_required(VERSION 2.8.9)

set(PROJECT_NAME "game_of_life")
project(${PROJECT_NAME})

find_package(Git REQUIRED)

# BOOST:

if(APPLE)
	set(Boost_INCLUDE_DIRS /opt/local/include)
	set(Boost_LIBRARY_DIRS /opt/local/lib)
	find_package(Boost COMPONENTS program_options system filesystem date_time regex thread REQUIRED)
	include_directories(${Boost_INCLUDE_DIRS})
	link_directories(${Boost_LIBRARY_DIRS})
elseif(UNIX)
	message (STATUS "Not yet tested on UNIX")
endif()

# OpenMP:

find_package(OpenMP)
if (OPENMP_FOUND)
	message (STATUS "OpenMP found")
	set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
	set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS} -std=c++11")
else()
	message (STATUS "OpenMP NOT found")
endif()

# Project structure:

include_directories(include)

add_subdirectory(source)
add_subdirectory(unit_test)