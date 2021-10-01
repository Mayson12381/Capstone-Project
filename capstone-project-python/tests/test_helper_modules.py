import unittest

from helper_modules.video_processor import read_image_from_video_stream
from numpy import ndarray


class TestVideoProcessor(unittest.TestCase):
    def test_read_image_from_video_stream(self):
        """
        Test that the function returns an image from the provided camera idm has correct type and shape
        """
        test_frame = read_image_from_video_stream(0)
        self.assertIsInstance(test_frame, ndarray)
        self.assertEqual(test_frame.shape, (1080, 1920, 3))
