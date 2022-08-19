from rosreact_tests.camera.opencv_camera import OpencvCamera
from sensor_msgs.msg import Image
from mock import Mock


def cleanup_after_fail(camera):
    try:
        camera.shutdown()
    finally:
        assert False


def test_shutdown():
    camera = OpencvCamera(0)
    camera.setup()
    camera.shutdown()
    assert not camera._cap.isOpened()


def test_failing_setup():
    camera = OpencvCamera("Not a camera")
    try:
        camera.setup()
    except IOError:
        pass
    else:
        cleanup_after_fail(camera)


def test_context_manager():
    with OpencvCamera(0):
        pass


def test_failing_context_manager():
    try:
        with OpencvCamera("not a camera"):
            assert False
    except IOError:
        pass


def test_read():
    with OpencvCamera(0) as camera:
        image = camera.read()
        assert type(image) == Image


def test_read_failure():
    cap = Mock()
    cap.read.return_value = (False, None)
    camera = OpencvCamera(0)
    camera._cap = cap
    try:
        camera.read()
        assert False
    except IOError:
        pass
