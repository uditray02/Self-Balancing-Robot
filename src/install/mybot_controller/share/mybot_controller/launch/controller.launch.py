from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument , GroupAction
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition

def generate_launch_description():
    
    #3 args
    
    use_python_arg = DeclareLaunchArgument(
        "use_python",
        default_value="False"
    )
    
    wheel_radius_arg = DeclareLaunchArgument(
        "wheel_radius",
        default_value="0.033"
    )
    
    wheel_separation_arg = DeclareLaunchArgument(
        "wheel_separation",
        default_value="0.17" 
    )
    
    use_simple_controller_arg = DeclareLaunchArgument(
        "use_simple_controller",
        default_value="True" 
    )
    
    
    #runtime value
    use_python = LaunchConfiguration("use_python")
    wheel_radius = LaunchConfiguration("wheel_radius")
    wheel_separation = LaunchConfiguration("wheel_separation")
    use_simple_controller = LaunchConfiguration("use_simple_controller") #new 
    
    
    
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
        ]
    )
    
    #controllers but we dont always want to start the mybot_con , we want to start the simple_vel_con too. Condition should be implemented...
    
    #start the NEW controller - mybot - myb_con   - # 2
    wheel_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "mybot_controller",
            "--controller-manager",
            "/controller_manager"
        ],
        condition=UnlessCondition(use_simple_controller)
    )
    
    simple_controller = GroupAction(
        condition=IfCondition(use_simple_controller),
        actions=[
            Node(
        package="controller_manager",
                executable="spawner",
                arguments=[
                    "simple_velocity_controller",
                    "--controller-manager",
                    "/controller_manager"
                ]
                
            ),
    
    #instances of node class
            Node(
                package="mybot_controller",
                executable="simple_controller.py",
                parameters=[{"wheel_radius": wheel_radius,
                            "wheel_separation": wheel_separation}],
                
                #condition=IfCondition(use_python)
            )
            
                ]
            ),

    
    
    
    return LaunchDescription([
        use_python_arg,
        wheel_radius_arg,
        wheel_separation_arg,
        use_simple_controller_arg,
        joint_state_broadcaster_spawner,
        simple_controller,
        wheel_controller_spawner,
         
    ])