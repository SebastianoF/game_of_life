"""
Hello world module to check if the libraries are all in place and the wrappers
of boost:::python are working.
"""
import sys, os


if __name__ == "__main__":

    dir_path = os.path.dirname(os.path.realpath(__file__))
    project_path = os.path.split(dir_path)[0]
    cpp_hello_world_omp_code = os.path.join(project_path, 'src/core/cpp_build/HelloWorldOMP')

    sys.path.insert(0, cpp_hello_world_omp_code)

    import helloOMP

    helloOMP.greetOMP()
