import rclpy
from my_custom_topic_msg.msg import MyMessage
from rclpy.node import Node


class MyPublisherNode(Node):
    def __init__(self):
        super().__init__("my_publisher_node")

        self.publisher = self.create_publisher(MyMessage, "my_custom_topic", 10)

        self.timer = self.create_timer(1, self.on_tick)

    def on_tick(self):
        msg = MyMessage()
        msg.x = 10
        msg.y = 20

        self.publisher.publish(msg)

        self.get_logger().info("Publish : " + str(msg.x) + ", " + str(msg.y))


def main(args=None):
    rclpy.init(args=args)
    node = MyPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
