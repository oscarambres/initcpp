# initcpp

initcpp is a script for bootstrapping a minimal C++ project based on CMake. The end result is a directory with the following contents:

```
main.cpp
.gitignore
CMakeLists.txt
README.md
tests/
  catch.hpp
  main.cpp
  CMakeLists.txt
build/
``` 

It performs the following steps:

1. Creates a directory with the name of the project and all the contents listed above (except `catch.hpp`).
2. Downloads `catch.hpp` from the official GitHub repository.
3. Calls `cmake ..` from the `build` directory.
4. Compiles the project.
