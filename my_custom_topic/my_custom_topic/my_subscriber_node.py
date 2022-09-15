import rclpy
from my_custom_topic_msg.msg import MyMessage
from rclpy.node import Node


class MySubscriberNode(Node):
    def __init__(self):
        super().__init__("my_subscriber_node")
        self.subscription = self.create_subscription(
            MyMessage, "my_custom_topic", self.on_subscribe, 10
        )

    def on_subscribe(self, msg):
        self.get_logger().info("Subscribe : " + str(msg.x) + "," + str(msg.y))


def main(args=None):
    rclpy.init(args=args)
    node = MySubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
