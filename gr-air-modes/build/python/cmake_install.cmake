# Install script for directory: /Users/apple/gr-air-modes/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages/air_modes" TYPE FILE FILES
    "/Users/apple/gr-air-modes/python/__init__.py"
    "/Users/apple/gr-air-modes/python/altitude.py"
    "/Users/apple/gr-air-modes/python/az_map.py"
    "/Users/apple/gr-air-modes/python/cpr.py"
    "/Users/apple/gr-air-modes/python/html_template.py"
    "/Users/apple/gr-air-modes/python/mlat.py"
    "/Users/apple/gr-air-modes/python/exceptions.py"
    "/Users/apple/gr-air-modes/python/flightgear.py"
    "/Users/apple/gr-air-modes/python/gui_model.py"
    "/Users/apple/gr-air-modes/python/kml.py"
    "/Users/apple/gr-air-modes/python/parse.py"
    "/Users/apple/gr-air-modes/python/msprint.py"
    "/Users/apple/gr-air-modes/python/radio.py"
    "/Users/apple/gr-air-modes/python/raw_server.py"
    "/Users/apple/gr-air-modes/python/rx_path.py"
    "/Users/apple/gr-air-modes/python/sbs1.py"
    "/Users/apple/gr-air-modes/python/sql.py"
    "/Users/apple/gr-air-modes/python/types.py"
    "/Users/apple/gr-air-modes/python/zmq_socket.py"
    "/Users/apple/gr-air-modes/python/Quaternion.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/site-packages/air_modes" TYPE FILE FILES
    "/Users/apple/gr-air-modes/build/python/__init__.pyc"
    "/Users/apple/gr-air-modes/build/python/altitude.pyc"
    "/Users/apple/gr-air-modes/build/python/az_map.pyc"
    "/Users/apple/gr-air-modes/build/python/cpr.pyc"
    "/Users/apple/gr-air-modes/build/python/html_template.pyc"
    "/Users/apple/gr-air-modes/build/python/mlat.pyc"
    "/Users/apple/gr-air-modes/build/python/exceptions.pyc"
    "/Users/apple/gr-air-modes/build/python/flightgear.pyc"
    "/Users/apple/gr-air-modes/build/python/gui_model.pyc"
    "/Users/apple/gr-air-modes/build/python/kml.pyc"
    "/Users/apple/gr-air-modes/build/python/parse.pyc"
    "/Users/apple/gr-air-modes/build/python/msprint.pyc"
    "/Users/apple/gr-air-modes/build/python/radio.pyc"
    "/Users/apple/gr-air-modes/build/python/raw_server.pyc"
    "/Users/apple/gr-air-modes/build/python/rx_path.pyc"
    "/Users/apple/gr-air-modes/build/python/sbs1.pyc"
    "/Users/apple/gr-air-modes/build/python/sql.pyc"
    "/Users/apple/gr-air-modes/build/python/types.pyc"
    "/Users/apple/gr-air-modes/build/python/zmq_socket.pyc"
    "/Users/apple/gr-air-modes/build/python/Quaternion.pyc"
    "/Users/apple/gr-air-modes/build/python/__init__.pyo"
    "/Users/apple/gr-air-modes/build/python/altitude.pyo"
    "/Users/apple/gr-air-modes/build/python/az_map.pyo"
    "/Users/apple/gr-air-modes/build/python/cpr.pyo"
    "/Users/apple/gr-air-modes/build/python/html_template.pyo"
    "/Users/apple/gr-air-modes/build/python/mlat.pyo"
    "/Users/apple/gr-air-modes/build/python/exceptions.pyo"
    "/Users/apple/gr-air-modes/build/python/flightgear.pyo"
    "/Users/apple/gr-air-modes/build/python/gui_model.pyo"
    "/Users/apple/gr-air-modes/build/python/kml.pyo"
    "/Users/apple/gr-air-modes/build/python/parse.pyo"
    "/Users/apple/gr-air-modes/build/python/msprint.pyo"
    "/Users/apple/gr-air-modes/build/python/radio.pyo"
    "/Users/apple/gr-air-modes/build/python/raw_server.pyo"
    "/Users/apple/gr-air-modes/build/python/rx_path.pyo"
    "/Users/apple/gr-air-modes/build/python/sbs1.pyo"
    "/Users/apple/gr-air-modes/build/python/sql.pyo"
    "/Users/apple/gr-air-modes/build/python/types.pyo"
    "/Users/apple/gr-air-modes/build/python/zmq_socket.pyo"
    "/Users/apple/gr-air-modes/build/python/Quaternion.pyo"
    )
endif()

