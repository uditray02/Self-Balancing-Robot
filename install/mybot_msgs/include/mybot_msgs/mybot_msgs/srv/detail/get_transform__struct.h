// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from mybot_msgs:srv/GetTransform.idl
// generated code does not contain a copyright notice

#ifndef MYBOT_MSGS__SRV__DETAIL__GET_TRANSFORM__STRUCT_H_
#define MYBOT_MSGS__SRV__DETAIL__GET_TRANSFORM__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'frame_id'
// Member 'child_frame_id'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/GetTransform in the package mybot_msgs.
typedef struct mybot_msgs__srv__GetTransform_Request
{
  /// The ID of the reference frame from which the transformation is requested.
  rosidl_runtime_c__String frame_id;
  /// The ID of the target frame to which the transformation is requested.
  rosidl_runtime_c__String child_frame_id;
} mybot_msgs__srv__GetTransform_Request;

// Struct for a sequence of mybot_msgs__srv__GetTransform_Request.
typedef struct mybot_msgs__srv__GetTransform_Request__Sequence
{
  mybot_msgs__srv__GetTransform_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} mybot_msgs__srv__GetTransform_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'transform'
#include "geometry_msgs/msg/detail/transform_stamped__struct.h"

/// Struct defined in srv/GetTransform in the package mybot_msgs.
typedef struct mybot_msgs__srv__GetTransform_Response
{
  /// Response
  ///  The transformation from the frame_id to the child_frame_id. This includes translation and rotation information.
  geometry_msgs__msg__TransformStamped transform;
  /// A boolean flag indicating whether the transformation was successful or not.
  bool success;
} mybot_msgs__srv__GetTransform_Response;

// Struct for a sequence of mybot_msgs__srv__GetTransform_Response.
typedef struct mybot_msgs__srv__GetTransform_Response__Sequence
{
  mybot_msgs__srv__GetTransform_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} mybot_msgs__srv__GetTransform_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MYBOT_MSGS__SRV__DETAIL__GET_TRANSFORM__STRUCT_H_
