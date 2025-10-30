import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class SimpleTurtleSimKinematics(Node):
    def __init__(self):
        super().__init__("simple_turtlesim_kinematics")
        
        
        self.turtle1_pose_sub = self.create_subscription(Pose, "/turle1/pose", self.turtle1PoseCallback, 10)
        
        self.turtle2_pose_sub = self.create_subscription(Pose, "/mbappeturtle2/pose", self.turtle2PoseCallback, 10)
        
        self.last_turtle1_pose_ = Pose()
        self.last_mbappeturtle2_pose_ = Pose()
        
    def turtlePoseCallback(self, msg):
        self.last_turtle1_pose_ = msg
    
    
    def turtle2PoseCallback(self, msg):
        self.last_mbappeturtle2_pose_ = msg
        
        Tx = self.last_mbappeturtle2_pose_.x - self.last_turtle1_pose_.x
        Ty = self.last_mbappeturtle2_pose_.y - self.last_turtle1_pose_.y
        
        #print the results of the calculation
        self.get_logger().info("""\n 
                               Translation Vector turtle1 -> mbappeturtle \n
                               Tx: %f \n
                               Ty: %f \n""" % (Tx, Ty))
        
def main():
    rclpy.init()
    simple_turtlesim_kinematics = SimpleTurtleSimKinematics()
    rclpy.spin(simple_turtlesim_kinematics)
    simple_turtlesim_kinematics.destroy_node()
    rclpy.shutdowm()


if __name__ == '__main__':
    main()
        
        