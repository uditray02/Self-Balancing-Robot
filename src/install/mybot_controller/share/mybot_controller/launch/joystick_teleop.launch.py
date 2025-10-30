from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="joystick",
        parameters=[os.path.join(get_package_share_directory("mybot_controller"), "config", "joy_config.yaml")],
    )
    
    #converting to TwistStamped kind of messages
    
    joy_teleop = Node(
        package="joy_teleop",
        executable="joy_teleop",
        parameters=[os.path.join(get_package_share_directory("mybot_controller"), "config", "joy_teleop.yaml")],
    )
    
    return LaunchDescription([
        joy_node,
        joy_teleop
        
    ])