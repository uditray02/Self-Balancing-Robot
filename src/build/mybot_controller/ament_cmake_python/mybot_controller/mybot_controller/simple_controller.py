#!/usr/bin/env python3

# Import necessary modules from the ROS2 Python client library
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import TwistStamped
import numpy as np


# Define a class 'SimpleController' that inherits from the 'Node' class in ROS2
class SimpleController(Node):  # Implements ROS2 node
    def __init__(self):
        super().__init__("simple_controller")  # Initialize the node with the name "simple_controller"
        
        # Declare parameters for the node with default values
        self.declare_parameter("wheel_radius", 0.033)  # Declare parameter for wheel radius
        self.declare_parameter("wheel_separation", 0.17)  # Declare parameter for wheel separation
        
        # Retrieve the values of the parameters and store them in class attributes
        self.wheel_radius_ = self.get_parameter("wheel_radius").get_parameter_value().double_value
        self.wheel_separation_ = self.get_parameter("wheel_separation").get_parameter_value().double_value
        
        # Log the values of the parameters using the node's logger
        self.get_logger().info("Using wheel radius: %f" % self.wheel_radius_)
        self.get_logger().info("Using wheel separation: %f" % self.wheel_separation_)
        
        # Create a publisher to send wheel commands, using Float64MultiArray messages
        self.wheel_cmd_pub_ = self.create_publisher(Float64MultiArray, "simple_velocity_controller/commands", 10)
        
        # Create a subscription to receive velocity commands, using TwistStamped messages
        self.vel_sub_ = self.create_subscription(TwistStamped, "mybot_controller/cmd_vel", self.velCallback, 10)
        
        # Placeholder for the differential drive robot kinematics matrix to convert vel from the robot's RF to the rotation of the 2 wheels
        self.speed_conversion_ = np.array([[self.wheel_radius_/2, self.wheel_radius_/2],
                                           [self.wheel_radius_/self.wheel_separation_, -self.wheel_radius_/self.wheel_separation_]])
        
        #displaying in terminal
        self.get_logger().info("The final conversion matrix is %s" %self.speed_conversion_)
        
        #message type = TwistStamp.. - contains command for linear and actual velocity
        
        
         
        
        
    # Define the callback function to handle incoming velocity commands
    def velCallback(self, msg):
        #creating a new numpy array
        robot_speed = np.array(([msg.twist.linear.x],
                                [msg.twist.angular.z]))
        
        #storing and calculating the inverse matrix
        wheel_speed = np.matmul(np.linalg.inv(self.speed_conversion_), robot_speed)
        wheel_speed_msg = Float64MultiArray()
        wheel_speed_msg.data = [wheel_speed[1, 0], wheel_speed[0, 0]]
        self.wheel_cmd_pub_.publish(wheel_speed_msg)
        
        
def main():
    rclpy.init()
    simple_controller = SimpleController()
    rclpy.spin(simple_controller)
    simple_controller.destroy_node()
    rclpy.shutdown() 
    
    
if __name__ == '__main__':
    main()