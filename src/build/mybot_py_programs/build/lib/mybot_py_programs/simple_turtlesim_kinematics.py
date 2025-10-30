import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
import math

class SimpleTurtleSimKinematics(Node):
    def __init__(self):
        super().__init__("simple_turtlesim_kinematics")

        # Ensure the topic names are correct
        self.turtle1_pose_sub = self.create_subscription(Pose, "/turtle1/pose", self.turtle1PoseCallback, 10)
        self.turtle2_pose_sub = self.create_subscription(Pose, "/mbappeturtle2/pose", self.turtle2PoseCallback, 10)

        self.last_turtle1_pose_ = Pose()
        self.last_mbappeturtle2_pose_ = Pose()

        # Debug logs to confirm initialization
        self.get_logger().info("SimpleTurtleSimKinematics node has been initialized")

    def turtle1PoseCallback(self, msg):
        self.last_turtle1_pose_ = msg
        self.get_logger().info(f"Turtle1 Pose: x={msg.x}, y={msg.y}, theta={msg.theta}")

    def turtle2PoseCallback(self, msg):
        self.last_mbappeturtle2_pose_ = msg
        self.get_logger().info(f"Turtle2 Pose: x={msg.x}, y={msg.y}, theta={msg.theta}")

        # Translation matrix calculation
        Tx = self.last_mbappeturtle2_pose_.x - self.last_turtle1_pose_.x
        Ty = self.last_mbappeturtle2_pose_.y - self.last_turtle1_pose_.y

        # Rotation matrix calculation
        theta_rad = self.last_mbappeturtle2_pose_.theta - self.last_turtle1_pose_.theta
        theta_deg = 180 * theta_rad / math.pi

        # Print the results of the calculation
        self.get_logger().info("""\n
                               Translation Vector turtle1 -> mbappeturtle \n
                               Tx: %f \n
                               Ty: %f \n
                               Rotational Matrix turtle1 -> mbappeturtle\n
                               theta(rad): %f\n
                               theta(deg): %f\n
                               |R11       R12| : |%f      %f|\n
                               |R21       R22| : |%f      %f|\n""" % (Tx, Ty, theta_rad, theta_deg, 
                                                                      math.cos(theta_rad), -math.sin(theta_rad), 
                                                                      math.sin(theta_rad), math.cos(theta_rad)))
        
def main(args=None):
    rclpy.init(args=args)
    simple_turtlesim_kinematics = SimpleTurtleSimKinematics()
    rclpy.spin(simple_turtlesim_kinematics)
    simple_turtlesim_kinematics.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
