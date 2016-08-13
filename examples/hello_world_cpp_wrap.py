import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
project_path = os.path.split(dir_path)[0]
cpp_hello_world_code = os.path.join(project_path, 'src/core/cpp_build/HelloWorld')
cpp_hello_box_code = os.path.join(project_path, 'src/core/cpp_build/HelloBox')

sys.path.insert(0, cpp_hello_world_code)
sys.path.insert(0, cpp_hello_box_code)

import hello
import hello_box

print 'This "' + hello.greet() + '" is from a C++ piece of code, build in the folder \n' + cpp_hello_world_code

my_box = hello_box.Box()

print my_box.height
my_box.height = 0.5
print my_box.height

my_box.path_to_file = "asdf_fdsa"
print my_box.path_to_file