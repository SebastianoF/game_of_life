import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
project_path = os.path.split(dir_path)[0]
cpp_hello_world_code = os.path.join(project_path, 'src/core/cpp_build/HelloWorld')
cpp_hello_member_code = os.path.join(project_path, 'src/core/cpp_build/HelloMember')

sys.path.insert(0, cpp_hello_world_code)
sys.path.insert(0, cpp_hello_member_code)

import hello
import member

print 'This "' + hello.greet() + '" is from a C++ piece of code, build in the folder \n' + cpp_hello_world_code

m1 = member.SomeClass("Pavel")
print "name =", m1.name
m1.name = "Guenther"
print "name = ", m1.name

m1.number = -56.5
print "number = ", m1.number