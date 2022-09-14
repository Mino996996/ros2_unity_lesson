import rclpy
from rclpy.node import Node


def main():
    rclpy.init()
    node = Node("hello_node")
    node.get_logger().info("Hello_World!")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
