import rclpy
from rclpy.node import Node
from mybot_msgs.srv import AddTwoInts

class SimpleServiceServer(Node):
    def __init__(self):
        super().__init__("simple_service_server")
        
        # new variable creation - service
        # creating new interface
        self.service_ = self.create_service(AddTwoInts, "add_two_ints", self.serviceCallBack)  # assigning names after the service is necessary so that the ros nodes can make contact with each other and also a callback function.
        
        # concluding the constructor of simple service server class 
        self.get_logger().info("Service named add_two_ints is fully ready. Please check")
    
    # Defining the function %d int, %req.a, req.b - Print the message sum
    def serviceCallBack(self, req, res):
        self.get_logger().info("Please Check!! NEW REQUEST RECEIVED a: %d, b: %d" % (req.a, req.b))
        
        # storing in the response message and in the sum variable
        res.sum = req.a + req.b 
        
        # print message in terminal
        self.get_logger().info("Please Check!! RETURNING THE SUM OF: %d" % res.sum)
        
        return res

def main():
    rclpy.init()
    simple_service_server = SimpleServiceServer()
    rclpy.spin(simple_service_server)
    rclpy.shutdown()        

if __name__ == '__main__':
    main()
