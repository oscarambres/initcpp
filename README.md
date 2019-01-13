# initcpp

A python script for quickly creating a new CMake based C++ project, with Catch2 as the testing framework. It creates the following tree of files:

```
project_name/
  main.cpp
  .gitignore
  CMakeLists.txt
  tests/
    catch.hpp
    main.cpp
    CMakeLists.txt
  build/
``` 

Then runs `cmake` on the `build` directory and compiles the project.