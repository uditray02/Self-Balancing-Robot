import rclpy
from rclpy.node import Node
from mybot_msgs.srv import AddTwoInts
import sys  #we have to make the two numbers parameter of the function - access the parameters of the main

class SimpleServiceClient(Node):
    def __init__(self, a, b):
        super().__init__("simple_service_client")
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")  # creating client for the service   (;add-two_int still doesnot exist in ROS)
        while not self.client_.wait_for_service(timeout_sec=1.0):   #if this function doesnot return TRue, we are not gonna proceed
            self.get_logger().info("Service not available, waiting again...")
            self.get_logger().info("Service available after %d attempts.", 10)
            
        #creating the new msg req we want to send to the service
        self.req_ = AddTwoInts.Request()
        #assigning a value here
        self.req_.a = a
        self.req_.b = b
        
        #callasync sends the request message  to the service server  and immediately returns    a result (not the actual result)
        
        self.future_ = self.client_.call_async(self.req_)  # this function will return a future object which we will use to check if the call is done or not
        # self.future_ = add_done_callback(self.responseCallBack)
        
        
        # we are going to use a loop here to check if the call is done or not
        while not self.future_.done():
            self.get_logger().info("Waiting for the response...")
            rclpy.spin_once(self)
        
        # checking if the call was successful or not
        if self.future_.result() is not None:
            self.get_logger().info("The sum of %d and %d is: %d" % (self.req_.a, self.req_.b, self.future_.result().sum))
        else:
            self.get_logger().info("Service call failed")
            

def main():
    rclpy.init()
    
    #verifying whether this script is been started with the correct number of parameters
    
    if len(sys.argv) != 3:
        print("WRONG No of ARGS! Usage: simple_service_client A B")
        return -1  #if script started with wrong number of args
    
    # Correcting the int conversion for each argument
    simple_service_client = SimpleServiceClient(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin(simple_service_client)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
