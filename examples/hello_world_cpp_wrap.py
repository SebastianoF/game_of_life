import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
project_path = os.path.split(dir_path)[0]
cpp_hello_world_code = os.path.join(project_path, 'src/core/cpp_build/HelloWorld')

sys.path.insert(0, cpp_hello_world_code)

import hello

print 'This "' + hello.greet() + '" is from a C++ piece of code, build in the folder \n' + cpp_hello_world_code