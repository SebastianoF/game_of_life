PYTHON_ADD_MODULE(state_manager state_manager.cpp)
IF (OPENMP_FOUND)
    PYTHON_ADD_MODULE(state_manager_omp state_manager_omp.cpp)
ENDIF()
