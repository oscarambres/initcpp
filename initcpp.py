#!/usr/bin/env python3

import os
import argparse
import urllib.request
import shutil
import sys
import subprocess

MAIN = '''#include <iostream>

int main() {

  return 0;
}
'''

MAIN_TESTS = '''#define CATCH_CONFIG_MAIN
#include "catch.hpp"
'''

CMAKELISTS = '''cmake_minimum_required(VERSION 3.1.0)

project($1)
set(CMAKE_CXX_STANDARD $2)
include(CTest)

add_executable($1 main.cpp)

if(BUILD_TESTING)
  add_subdirectory(tests)
  add_test(t_$1 ${CMAKE_BINARY_DIR}/tests/t_$1)
endif()
'''

CMAKELISTS_TESTS = '''cmake_minimum_required(VERSION 3.1.0)

set(CMAKE_CXX_STANDARD $2)

add_executable(t_$1 main.cpp)

include_directories(t_$1 ${CMAKE_SOURCE_DIR})
'''

GIT_IGNORE = '''build
'''

CATCH_URL = 'https://raw.githubusercontent.com/catchorg/Catch2/master/single_include/catch2/catch.hpp'

p = argparse.ArgumentParser()
p.add_argument('project', help='Project name.')
p.add_argument('-s', help='C++ standard to use.', type=int, choices=[98, 11, 14], default=14)
args = p.parse_args()

PROJECT = args.project
TESTS = 'tests'
BUILD = 'build'
STD = str(args.s)

try:
  os.mkdir(PROJECT)
except FileExistsError:
  print('Project "' + PROJECT + '" already exists')
  sys.exit(1)

os.mkdir(os.path.join(PROJECT, TESTS))
os.mkdir(os.path.join(PROJECT, BUILD))

print('{0: <23}'.format('Creating project files'), end='', flush=True)

with open(os.path.join(PROJECT, 'main.cpp'), 'w') as f:
  f.write(MAIN)

with open(os.path.join(PROJECT, 'CMakeLists.txt'), 'w') as f:
  f.write(CMAKELISTS.replace('$1', PROJECT).replace('$2', STD))

with open(os.path.join(PROJECT, '.gitignore'), 'w') as f:
  f.write(GIT_IGNORE)

with open(os.path.join(PROJECT, TESTS, 'main.cpp'), 'w') as f:
  f.write(MAIN_TESTS)

with open(os.path.join(PROJECT, TESTS, 'CMakeLists.txt'), 'w') as f:
  f.write(CMAKELISTS_TESTS.replace('$1', PROJECT).replace('$2', STD))

print('\U00002714') 
print('{0: <23}'.format('Downloading catch2'), end='', flush=True)
try:
  resp = urllib.request.urlopen(CATCH_URL)
  with open(os.path.join(PROJECT, TESTS, 'catch.hpp'), 'w') as f:
    f.write(resp.read().decode('utf-8'))
  print('\U00002714') 
except urllib.error.URLError as e:
  print('\U00002718') 
  print(str(e) + ': ' + CATCH_URL)
  shutil.rmtree(PROJECT)
  sys.exit(1)

print('{0: <23}'.format('Running cmake'), end='', flush=True)
try:
  r = subprocess.run(['cmake', '-B', os.path.join(PROJECT, BUILD), '-S', PROJECT], capture_output=True)
  if r.returncode == 0:
    print('\U00002714') 
    print('{0: <23}'.format('Compiling project'), end='', flush=True)
    t = subprocess.run(['make', '-C', os.path.join(PROJECT, BUILD)], capture_output=True)
    if t.returncode == 0:
      print('\U00002714') 
    else:
      print('\U00002718') 
      sys.exit(1)
  else:
    print('\U00002718') 
    sys.exit(1)
except Exception as e:
  print('\U00002718') 
  print(e)
  sys.exit(1)

print('Created project "' + PROJECT + '"')
