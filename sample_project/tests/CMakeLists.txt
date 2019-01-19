cmake_minimum_required(VERSION 3.1.0)

set(CMAKE_CXX_STANDARD 14)

add_executable(t_sample_project main.cpp)

include_directories(t_sample_project ${CMAKE_SOURCE_DIR})
