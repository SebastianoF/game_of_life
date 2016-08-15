"""
Hello world module to check if the libraries are all in place and the wrappers
of boost:::python are working.
"""
import sys, os


if __name__ == "__main__":

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

    my_box.height = 0.5
    my_box.width = 1.5
    my_box.length = 2.5

    my_box.file_path = os.path.join(project_path, 'data', 'box_info.txt')

    my_box.save_info()

    print "Check the file box_info.txt to see if everything works."
