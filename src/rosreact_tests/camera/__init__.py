from .node import Node
from .opencv_camera import OpencvCamera


def main(driver: str = "opencv"):
    if driver == "opencv":
        _opencv_main()
    else:
        raise ValueError("Requested unknown camera driver")


def _opencv_main():
    camera = OpencvCamera(0)
    n = Node(camera)
    n.start()
