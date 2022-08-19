from cv2 import VideoCapture
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from .camera import Camera
from typing import Union, Optional


class OpencvCamera(Camera):
    def __init__(self, source: Union[int, str]):
        self._source: Union[int, str] = source
        self._cap: Optional[VideoCapture] = None
        self._bridge: CvBridge = CvBridge()

    def setup(self) -> None:
        self._cap = VideoCapture(self._source)
        if not self._cap.isOpened():
            raise IOError(f"Could not open VideoCapture "
                          f"with source {self._source}")

    def read(self) -> Image:
        bool_result, image = self._cap.read()
        if not bool_result:
            raise IOError(f"Could not read new frame")
        return self._bridge.cv2_to_imgmsg(image, encoding='bgr8')

    def shutdown(self) -> None:
        self._cap.release()

    def __enter__(self):
        self.setup()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shutdown()
