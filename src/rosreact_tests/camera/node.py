import rospy
from sensor_msgs.msg import Image
from typing import Optional
from .camera import Camera


class Node:
    __slots__ = (
        '_publisher',
        '_camera',
        '_frequency',
    )

    def __init__(self, camera: Camera, frequency: float = 30.0):
        self._publisher: Optional[rospy.Publisher] = None
        self._camera: Camera = camera
        self._frequency: float = frequency

    def start(self) -> None:
        self._setup()
        self._loop()
        self._shutdown()

    def _setup(self) -> None:
        rospy.init_node("camera_node")
        self._publisher = rospy.Publisher(
            '/camera/image', Image, queue_size=1, latch=True,
        )
        self._camera.setup()

    def _loop(self) -> None:
        rate = rospy.Rate(self._frequency)
        while not rospy.is_shutdown():
            self._publish_image()
            rate.sleep()

    def _publish_image(self) -> None:
        try:
            new_image = self._camera.read()
        except IOError as e:
            rospy.logerr(e)
            return
        self._publisher.publish(new_image)

    def _shutdown(self) -> None:
        self._camera.shutdown()

    def __repr__(self):
        return f'Camera Node @{self._frequency:.1f} Hz'

    def __str__(self):
        return self.__repr__()
