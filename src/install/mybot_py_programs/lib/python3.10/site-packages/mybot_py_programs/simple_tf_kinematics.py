import rclpy
from rclpy.node import Node
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

#static transform will publish tf messages between base and top
#dynamic transform will publish tf messages every 0.1 seconds between odom and base

class SimpleTfKinematics(Node):
    def __init__(self):
        #base part
        super().__init__("simple_tf_kinematics")
        
        #To publish transform between two reference fixed frames in which the relative position and orientation dont change
        self.static_tf_broadcaster_ = StaticTransformBroadcaster(self)  #we can use this to publish the transform static tf
        self.dynamic_tf_broadcaster_ = TransformBroadcaster(self) #dynamic tf
        
        #TF static topic is called TransformStamped defined in Geometry msgs
        self.static_transform_stamped_ = TransformStamped()
        #dynamic tf
        self.dynamic_transform_stamped_ = TransformStamped()
        
        #support variables for simulation between odom and mainbase
        #indicates adding transform at any iteration of the timer
        self.x_increment_ = 0.05 #child frame id of dynamic will move 0.05cms
        self.last_x_ = 0.00 #contains the last main value of the x direction of the dynamic that used to calcualte the next values
        
        #dynamic transform to publish repeatedly after the get_logger function(line 59)
        
        
        #adding info about the time in which the transform is generated
        self.static_transform_stamped_.header.stamp = self.get_clock().now().to_msg()
        
        #defining the names of the two frames which are connected by the static transforms
        
        #defining the main base frame id
        self.static_transform_stamped_.header.frame_id = "mybot_base" #parent for static
        #defining the child frame id
        self.static_transform_stamped_.child_frame_id = "mybot_top"
        
        #Characteristics of this connection to define now
        
        #translation vectors
        self.static_transform_stamped_.transform.translation.x = 0.0
        self.static_transform_stamped_.transform.translation.y = 0.0
        self.static_transform_stamped_.transform.translation.z = 0.3  # making the top frame 30cms away from the base of the mybot which is the MODEL
        
        #representation of the orientations are done using Quaternions
        #Instead of rotational matrices, Euler angles are also used to define the same.
        
        #rotational vectors
        #Quaternions are composed of 4 components and down below we are defining those components(x4)
        #By this - The simple transform between the two frames are done.......
        self.static_transform_stamped_.transform.rotation.x = 0.0  # empty rotation setting
        self.static_transform_stamped_.transform.rotation.y = 0.0
        self.static_transform_stamped_.transform.rotation.z = 0.0
        self.static_transform_stamped_.transform.rotation.w = 1.0 
        
        #info adding to the dynamic transform which we know 
        self.dynamic_transform_stamped_.header.stamp = self.get_clock().now().to_msg()
        #setting the frame id *new frame*
        self.dynamic_transform_stamped_.header.frame_id = "odom" #odometry being new dynamic parent
        #child frame id
        self.dynamic_transform_stamped_.child_frame_id = "mybot_base"
        
        #using static_tf_broadcaster to publish the transform (calling) and sending the static transformed stamped message created above
        self.static_tf_broadcaster_.sendTransform(self.static_transform_stamped_)
        
        #printing a message to inform the user of correct transformation
        self.get_logger().info("Successfully stamped message published between %s and %s" %
                               (self.static_transform_stamped_.header.frame_id, self.static_transform_stamped_.child_frame_id))
        
        #creating a timer for dynamic transform to publish repeatedly
        self.timer_ = self.create_timer(0.1, self.timerCallBack) #every 0.1 seconds, a new transfor is going to be published
        
    def timerCallBack(self):
        self.dynamic_transform_stamped_.header.stamp = self.get_clock().now().to_msg() #current ROS2 time
        self.dynamic_transform_stamped_.header.frame_id = "odom" #parent fr dynamic
        self.dynamic_transform_stamped_.child_frame_id = "mybot_base" #child fr dynmic
        
        #properties
        self.dynamic_transform_stamped_.transform.translation.x = self.last_x_ + self.x_increment_ #lastvalue + increment
        self.dynamic_transform_stamped_.transform.translation.y = 0.0 
        self.dynamic_transform_stamped_.transform.translation.z = 0.0
        self.dynamic_transform_stamped_.transform.rotation.x = 0.0
        self.dynamic_transform_stamped_.transform.rotation.y = 0.0
        self.dynamic_transform_stamped_.transform.rotation.z = 0.0
        self.dynamic_transform_stamped_.transform.rotation.w = 1.0  #meaning both the odom and base will be oriented in the same way
        #for simulation between odom and base, support variables are required within constructor of the simple_tf_kinematics(line 24)
        
        #publishing in the tf topic
        self.dynamic_tf_broadcaster_.sendTransform(self.dynamic_transform_stamped_)
        
        #updating the last_x_ value
        self.last_x_ += self.x_increment_  #updating the last x position by adding increment value
        #self.last_x_ = self.dynamic_transform_stamped_.transform.translation.x
        


#defining and declaring the main function
def main():
    rclpy.init()
    simple_tf_kinematics = SimpleTfKinematics()
    rclpy.spin(simple_tf_kinematics)
    simple_tf_kinematics.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
