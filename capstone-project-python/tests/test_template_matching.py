import unittest

import cv2
from numpy import array, ndarray, round
from template_matching.template_matching import (_flip_image_horizontally,
                                                 _scale_image_horizontally,
                                                 _scale_image_vertically,
                                                 _black_out_image_except_roi,
                                                 _black_out_image_except_rgb_threshold,
                                                 _max_diff)

TEST_IMG = None


class TestTemplateMatching(unittest.TestCase):
    def setUp(self):
        global TEST_IMG
        TEST_IMG = cv2.imread('tests/test_images/test_image.jpg')

    def test_flip_image_horizontally(self):
        """
        Test if the image is flipped correctly and has correct dimensions and type
        """
        flipped_image = _flip_image_horizontally(TEST_IMG)
        self.assertEqual(array(flipped_image).size, array(cv2.flip(TEST_IMG, 1)).size)
        self.assertIsInstance(flipped_image, ndarray)
        self.assertEqual(TEST_IMG.shape, flipped_image.shape)

    
    def test_scale_image_horizontally(self):
        """
        Test if the image is scaled correctly and has correct type
        """
        scale_factor = 0.5
        scaled_image = _scale_image_horizontally(TEST_IMG, scale_factor)
        self.assertIsInstance(scaled_image, ndarray)
        self.assertEqual(TEST_IMG.shape[1] * scale_factor, scaled_image.shape[1])


    def test_scale_image_vertically(self):
        """
        Test if the image is scaled correctly and has correct type
        """
        scale_factor = 0.5
        scaled_image = _scale_image_vertically(TEST_IMG, scale_factor)
        self.assertIsInstance(scaled_image, ndarray)
        self.assertEqual(TEST_IMG.shape[0] * scale_factor, scaled_image.shape[0])


    def test_black_out_image_except_roi(self):
        """
        Test if the image is blacked out correctly and has correct type
        """
        roi_x = 0
        roi_y = 0
        roi_width = int(round(TEST_IMG.shape[1] * 0.5))
        roi_height = int(round(TEST_IMG.shape[0] * 0.5))
        blacked_out_image = _black_out_image_except_roi(TEST_IMG, roi_x, roi_y, roi_width, roi_height)
        self.assertIsInstance(blacked_out_image, ndarray)
        self.assertEqual(TEST_IMG.shape, blacked_out_image.shape)


    def test_black_out_image_except_rgb_threshold(self):
        """
        Test if the image is blacked out correctly and has correct type
        """
        threshold = 150
        blacked_out_image = _black_out_image_except_rgb_threshold(TEST_IMG, threshold)
        self.assertIsInstance(blacked_out_image, ndarray)
        self.assertEqual(TEST_IMG.shape, blacked_out_image.shape)


    def test_max_diff(self):
        """
        Test if the maxDiff is calculated correctly
        """
        same_numbers = [150, 150, 150]
        max_difference = _max_diff(same_numbers)
        self.assertEqual(max_difference, 0)
        different_numbers = [150, 150, 151]
        max_difference = _max_diff(different_numbers)
        self.assertEqual(max_difference, 1)
        very_different_numbers = [140, 151, 182]
        max_difference = _max_diff(very_different_numbers)
        self.assertEqual(max_difference, 42)
