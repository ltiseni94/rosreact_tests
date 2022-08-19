from abc import ABC, abstractmethod
from sensor_msgs.msg import Image


class Camera(ABC):
    @abstractmethod
    def setup(self) -> None:
        pass

    @abstractmethod
    def read(self) -> Image:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass
