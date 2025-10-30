import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter

class SimpleParameter(Node):
    def __init__(self):
        super().__init__("simple_parameter")
        
        self.counter_ = 0
        self.declare_parameter("simple_int_param" , 28)
        self.declare_parameter("simple_string_param" , "ROS ENGINEER")
        self.add_on_set_parameters_callback(self.paramChangeCallback)
        
    def paramChangeCallback(self, params):
        result = SetParametersResult()
        for param in params:
            if param.name == "simple_int_param" and param.type_ == Parameter.Type.INTEGER:
                self.get_logger().info("Integer parameter changed to %d" % param.value)
                result.successful = True
                
            if param.name == "simple_string_param" and param.type_ == Parameter.Type.STRING:
                self.get_logger().info("String parameter changed to %s" % param.value)
                result.successful = True
                
        return result
    
def main():
    rclpy.init()
    simple_parameter = SimpleParameter()
    rclpy.spin(simple_parameter)
    simple_parameter.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    
            
            