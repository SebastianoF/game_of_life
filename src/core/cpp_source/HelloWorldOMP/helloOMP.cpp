#include<omp.h>
#include<stdio.h>
#include<stdlib.h>

char const* greetOMP()
{
	#pragma omp parallel num_threads(6)
	{
		int tid = omp_get_thread_num();
		printf("Hello world from thread = %d \n",tid);
		if(tid == 0){
		    int nthreads = omp_get_num_threads();
		    printf("Number of threads = %d\n",nthreads);
		}
	}

   return "hello, world";
}

#include <boost/python.hpp>

BOOST_PYTHON_MODULE(helloOMP)
{
    using namespace boost::python;
    def("greetOMP", greetOMP);
}
