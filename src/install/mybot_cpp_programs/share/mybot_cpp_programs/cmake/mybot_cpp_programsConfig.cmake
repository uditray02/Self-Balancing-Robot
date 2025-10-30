# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_mybot_cpp_programs_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED mybot_cpp_programs_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(mybot_cpp_programs_FOUND FALSE)
  elseif(NOT mybot_cpp_programs_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(mybot_cpp_programs_FOUND FALSE)
  endif()
  return()
endif()
set(_mybot_cpp_programs_CONFIG_INCLUDED TRUE)

# output package information
if(NOT mybot_cpp_programs_FIND_QUIETLY)
  message(STATUS "Found mybot_cpp_programs: 0.0.0 (${mybot_cpp_programs_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'mybot_cpp_programs' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${mybot_cpp_programs_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(mybot_cpp_programs_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${mybot_cpp_programs_DIR}/${_extra}")
endforeach()
