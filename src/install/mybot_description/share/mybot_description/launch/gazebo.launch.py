from os import pathsep  # Import the pathsep constant for separating paths in environment variables
from launch import LaunchDescription  # Import the LaunchDescription class to define a launch description
from launch_ros.actions import Node  # Import the Node class to define ROS 2 nodes
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription  # Import necessary actions
import os  # Import the os module to interact with the operating system
from ament_index_python.packages import get_package_share_directory, get_package_prefix  # Import functions to get package directories
from launch_ros.parameter_descriptions import ParameterValue  # Import ParameterValue to define parameter values
from launch.substitutions import Command, LaunchConfiguration  # Import Command and LaunchConfiguration for substitutions
from launch.launch_description_sources import PythonLaunchDescriptionSource  # Import PythonLaunchDescriptionSource to include other launch files

def generate_launch_description():
    # Get the directory of the mybot_description package
    mybot_description = get_package_share_directory("mybot_description")
    mybot_description_prefix = get_package_prefix("mybot_description")

    # Construct the model path and update the GAZEBO_MODEL_PATH environment variable
    model_path = os.path.join(mybot_description, "models")
    model_path += pathsep + os.path.join(mybot_description_prefix, "share")

    # Set the GAZEBO_MODEL_PATH environment variable
    env_variable = SetEnvironmentVariable("GAZEBO_MODEL_PATH", model_path)

    # Declare a launch argument for the robot model file
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

    # Include the Gazebo server launch file
    start_gazebo_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gzserver.launch.py"))
    )

    # Include the Gazebo client launch file
    start_gazebo_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gzclient.launch.py"))
    )

    # Define a node to spawn the robot in Gazebo
    spawn_robot = Node(
        package="gazebo_ros",  # Package name
        executable="spawn_entity.py",  # Executable name
        arguments=["-entity", "mybot", "-topic", "robot_description"],  # Arguments to pass to the executable
        output="screen"  # Output configuration
    )

    # Return the launch description with all the actions
    return LaunchDescription([
        env_variable,  # Set environment variable for Gazebo model path
        model_arg,  # Declare model argument
        robot_state_publisher,  # Node to publish the robot state
        start_gazebo_server,  # Include Gazebo server launch file
        start_gazebo_client,  # Include Gazebo client launch file
        spawn_robot  # Node to spawn the robot in Gazebo
    ])
