// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mybot_msgs:srv/AddTwoInts.idl
// generated code does not contain a copyright notice

#ifndef MYBOT_MSGS__SRV__DETAIL__ADD_TWO_INTS__BUILDER_HPP_
#define MYBOT_MSGS__SRV__DETAIL__ADD_TWO_INTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "mybot_msgs/srv/detail/add_two_ints__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace mybot_msgs
{

namespace srv
{

namespace builder
{

class Init_AddTwoInts_Request_b
{
public:
  explicit Init_AddTwoInts_Request_b(::mybot_msgs::srv::AddTwoInts_Request & msg)
  : msg_(msg)
  {}
  ::mybot_msgs::srv::AddTwoInts_Request b(::mybot_msgs::srv::AddTwoInts_Request::_b_type arg)
  {
    msg_.b = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mybot_msgs::srv::AddTwoInts_Request msg_;
};

class Init_AddTwoInts_Request_a
{
public:
  Init_AddTwoInts_Request_a()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddTwoInts_Request_b a(::mybot_msgs::srv::AddTwoInts_Request::_a_type arg)
  {
    msg_.a = std::move(arg);
    return Init_AddTwoInts_Request_b(msg_);
  }

private:
  ::mybot_msgs::srv::AddTwoInts_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::mybot_msgs::srv::AddTwoInts_Request>()
{
  return mybot_msgs::srv::builder::Init_AddTwoInts_Request_a();
}

}  // namespace mybot_msgs


namespace mybot_msgs
{

namespace srv
{

namespace builder
{

class Init_AddTwoInts_Response_sum
{
public:
  Init_AddTwoInts_Response_sum()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::mybot_msgs::srv::AddTwoInts_Response sum(::mybot_msgs::srv::AddTwoInts_Response::_sum_type arg)
  {
    msg_.sum = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mybot_msgs::srv::AddTwoInts_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::mybot_msgs::srv::AddTwoInts_Response>()
{
  return mybot_msgs::srv::builder::Init_AddTwoInts_Response_sum();
}

}  // namespace mybot_msgs

#endif  // MYBOT_MSGS__SRV__DETAIL__ADD_TWO_INTS__BUILDER_HPP_
