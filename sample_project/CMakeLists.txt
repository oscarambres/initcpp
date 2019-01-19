cmake_minimum_required(VERSION 3.1.0)

project(sample_project)
set(CMAKE_CXX_STANDARD 14)
include(CTest)

add_executable(sample_project main.cpp)

if(BUILD_TESTING)
  add_subdirectory(tests)
  add_test(t_sample_project ${CMAKE_BINARY_DIR}/tests/t_sample_project)
endif()
