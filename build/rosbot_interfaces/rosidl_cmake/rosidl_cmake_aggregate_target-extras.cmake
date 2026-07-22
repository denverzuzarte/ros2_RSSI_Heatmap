# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target rosbot_interfaces::rosbot_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${rosbot_interfaces_TARGETS}.
if(rosbot_interfaces_TARGETS AND NOT TARGET rosbot_interfaces::rosbot_interfaces)
  add_library(rosbot_interfaces::rosbot_interfaces INTERFACE IMPORTED)
  set_target_properties(rosbot_interfaces::rosbot_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${rosbot_interfaces_TARGETS}")
endif()
