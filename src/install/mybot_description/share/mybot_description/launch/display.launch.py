# Import necessary classes and functions from the launch package
from launch import LaunchDescription  # Import the LaunchDescription class to define a launch description
from launch_ros.actions import Node  # Import the Node class to define ROS 2 nodes
from launch.actions import DeclareLaunchArgument  # Import the DeclareLaunchArgument class to declare launch arguments
import os  # Import the os module to interact with the operating system
from ament_index_python.packages import get_package_share_directory  # Import the function to get the package share directory
from launch_ros.parameter_descriptions import ParameterValue  # Import ParameterValue to define parameter values
from launch.substitutions import Command, LaunchConfiguration  # Import Command and LaunchConfiguration for substitutions

# Define a function to generate the launch description
def generate_launch_description():
    # Declare a launch argument for the model file path
    model_arg = DeclareLaunchArgument(
        name="model",  # Name of the argument
        default_value=os.path.join(get_package_share_directory("mybot_description"), "urdf", "mybot.urdf.xacro"),  # Default value pointing to the URDF file
        description="Absolute path to the robot's URDF file"  # Description of the argument
    )

    # Create a ParameterValue for the robot description by running xacro on the model file
    robot_description = ParameterValue(
        Command(["xacro ", LaunchConfiguration("model")]),  # Command to run xacro on the model file
        value_type=str  # Specify that the parameter value is of type string
    )

    # Define a node for the robot state publisher
    robot_state_publisher = Node(
        package="robot_state_publisher",  # Package name
        executable="robot_state_publisher",  # Executable name
        parameters=[{"robot_description": robot_description}]  # Pass the robot description parameter to the node
    )

    # Define a node for the joint state publisher GUI
    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",  # Package name
        executable="joint_state_publisher_gui"  # Executable name
    )

    # Define a node for RViz
    rviz_node = Node(
        package="rviz2",  # Package name
        executable="rviz2",  # Executable name
        name="rviz2",  # Name of the node
        output="screen",  # Output configuration
        arguments=["-d", os.path.join(get_package_share_directory("mybot_description"), "rviz", "display.rviz")]  # Arguments to run RViz with a specified configuration file
    )

    # Return the LaunchDescription with all defined launch arguments and nodes
    return LaunchDescription([
        model_arg,  # Include the model argument
        robot_state_publisher,  # Include the robot state publisher node
        joint_state_publisher_gui,  # Include the joint state publisher GUI node
        rviz_node  # Include the RViz node
    ])
