FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})

FIND_PACKAGE(PythonLibs)
INCLUDE_DIRECTORIES(
    ${CMAKE_SOURCE_DIR}
    ${PYTHON_INCLUDE_PATH}
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${LEMON_INCLUDE_DIRS}
)

# SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -std=c++11 -Wall -Wfatal-errors")

SET(CMAKE_SWIG_FLAGS "")

SET_SOURCE_FILES_PROPERTIES(openql.i PROPERTIES CPLUSPLUS ON)
# SET_SOURCE_FILES_PROPERTIES(openql.i PROPERTIES SWIG_FLAGS "-includeall")
# SWIG_ADD_MODULE(openql python openql.i openql.cxx)
SWIG_ADD_MODULE(openql python openql.i)
# SWIG_ADD_LIBRARY(openql LANGUAGE python SOURCES openql.i TYPE SHARED)

SWIG_LINK_LIBRARIES(openql ${PYTHON_LIBRARIES} ${LEMON_LIBRARIES})

# ADD_EXECUTABLE(apiTest test.cc)
# TARGET_LINK_LIBRARIES(apiTest _openql.so)
