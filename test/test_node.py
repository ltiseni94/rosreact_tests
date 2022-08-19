from subprocess import Popen, TimeoutExpired, PIPE, STDOUT
from pathlib import Path
from typing import Optional
from mock import Mock
from rosreact_tests.camera.node import Node
from sensor_msgs.msg import Image
from multiprocessing import Process
import time


class TestNode:
    roscore_process: Optional[Popen] = None

    @classmethod
    def setup_class(cls):
        scripts_folder_path = Path(__file__).parent.parent / "scripts"
        cls.roscore_process = Popen(
            f"{scripts_folder_path}/start_roscore.bash",
            shell=True,
            stdout=PIPE,
            stderr=STDOUT,
        )

    @classmethod
    def teardown_class(cls):
        cls.roscore_process.terminate()
        try:
            cls.roscore_process.wait(3)
        except TimeoutExpired:
            cls.roscore_process.kill()

    def __init__(self):
        camera_mock = Mock()
        camera_mock.read.return_value = Image()
        self.node = Node(camera=camera_mock)

    def test_setup(self):
        self.node._setup()

    def test_shutdown(self):
        self.node._shutdown()

    def test_publish_image(self):
        self.node._setup()
        self.node._publish_image()

    def test_loop(self):
        p = Process(target=self.node.start)
        p.start()
        time.sleep(1)
        p.terminate()
