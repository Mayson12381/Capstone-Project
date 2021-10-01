import unittest
from typing import List
import os

import config
import cv2
from data_detection.detections import (_apply_detections_to_team_image,
                                       _get_player_detections,
                                       _get_team_detections_and_categories,
                                       load_model,
                                       _get_team_data_from_detections,
                                       _initialize_empty_team_data)
from data_detection.image_processor import (get_team_image_right,
                                            get_player_images_right,
                                            get_team_image_left,
                                            get_player_images_left)
from numpy import ndarray

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

TEST_IMG = None


class TestDetections(unittest.TestCase):
    def setUp(self):
        config.model = load_model()
        global TEST_IMG
        TEST_IMG = cv2.imread(os.path.join('tests', 'test_images', 'test_image.jpg'))

    def test_get_player_detections(self):
        """
        Test if the player image detections is returning correct types and correct label map
        """
        test_player_img, _, _, _, _ = get_player_images_right(TEST_IMG)
        player_detections, detection_categories = _get_player_detections(
            test_player_img)
        self.assertEqual(detection_categories[1], {'id': 1, 'name': 'AK-47'})
        self.assertIn('detection_classes', player_detections)
        self.assertIsInstance(player_detections['detection_classes'], ndarray)
        self.assertIn('detection_scores', player_detections)
        self.assertIsInstance(player_detections['detection_scores'], ndarray)
        
    def test_apply_detections_to_team_image(self):
        """
        Test if the returned image is correct type and correct shape
        """
        test_team_img = get_team_image_right(TEST_IMG, config.PLAYER_X_OFFSET,
                                             config.PLAYER_HEIGHT,
                                             config.PLAYER_Y_OFFSET)
        team_detections, detection_categories = _get_team_detections_and_categories(
            TEST_IMG, get_player_images_right)
        team_img_with_detections = _apply_detections_to_team_image(
            test_team_img, team_detections, detection_categories)
        self.assertIsInstance(team_img_with_detections, ndarray)
        self.assertEqual(team_img_with_detections.shape, test_team_img.shape)
        self.assertEqual(team_img_with_detections.shape[2], 3)

    def test_get_team_detections_and_categories(self):
        """
        Test if the team image detections is returning correct types and correct label map
        """
        team_detections, detection_categories = _get_team_detections_and_categories(
            TEST_IMG, get_player_images_right)
        self.assertEqual(detection_categories[1], {'id': 1, 'name': 'AK-47'})
        self.assertIn('detection_classes', team_detections[0])
        self.assertIsInstance(team_detections[0]['detection_classes'], ndarray)
        self.assertIn('detection_scores', team_detections[0])
        self.assertIsInstance(team_detections[0]['detection_scores'], ndarray)

    def test_get_team_data_from_detections(self):
        """
        Test if the team data is returned correctly for one player1 from test image (given the latest ML model)
        """
        team_detections, detection_categories = _get_team_detections_and_categories(
            TEST_IMG, get_player_images_right)
        team_data = _get_team_data_from_detections(team_detections,
                                                   detection_categories)
        self.assertEqual(team_data['player1']['weapon'], 'AWP')
        self.assertEqual(team_data['player1']['health_status'], 1)
        self.assertEqual(team_data['player1']['nades'], [])
        self.assertEqual(team_data['player1']['kevlar'], 'Helmet')

    def test_initialize_empty_team_data(self):
        """
        Test if the empty team data is returned correctly
        """
        team_data = _initialize_empty_team_data()
        self.assertEqual(team_data['player1']['weapon'], None)
        self.assertEqual(team_data['player1']['health_status'], 1)
        self.assertEqual(team_data['player1']['nades'], [])
        self.assertEqual(team_data['player1']['kevlar'], 'Helmet')


class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        config.model = load_model()
        TEST_IMG = cv2.imread('tests/test_images/test_image.jpg')

    def test_get_team_image_right(self):
        """
        Test if the player images are returned in correct shape and correct type
        """
        test_team_img = get_team_image_right(TEST_IMG, config.PLAYER_X_OFFSET,
                                             config.PLAYER_HEIGHT,
                                             config.PLAYER_Y_OFFSET)
        self.assertEqual(test_team_img.shape,
                         (config.PLAYER_HEIGHT * 5, config.PLAYER_WIDTH, 3))
        self.assertIsInstance(test_team_img, ndarray)

    def test_get_player_images_right_seperated(self):
        """
        Test if the player images are returned correctly
        """
        test_player_img, _, _, _, _ = get_player_images_right(
            TEST_IMG, config.PLAYER_X_OFFSET, config.PLAYER_HEIGHT,
            config.PLAYER_Y_OFFSET)
        self.assertEqual(test_player_img.shape,
                         (config.PLAYER_HEIGHT, config.PLAYER_WIDTH, 3))
        self.assertIsInstance(test_player_img, ndarray)

    def test_get_team_image_left(self):
        """
        Test if the player images are returned correctly
        """
        test_team_img = get_team_image_left(TEST_IMG, config.PLAYER_X_OFFSET,
                                            config.PLAYER_HEIGHT,
                                            config.PLAYER_Y_OFFSET)
        self.assertEqual(test_team_img.shape,
                         (config.PLAYER_HEIGHT * 5, config.PLAYER_WIDTH, 3))
        self.assertIsInstance(test_team_img, ndarray)

    def test_get_player_images_left(self):
        """
        Test if the player images are returned correctly
        """
        test_player_img, _, _, _, _ = get_player_images_left(
            TEST_IMG, config.PLAYER_X_OFFSET, config.PLAYER_HEIGHT,
            config.PLAYER_Y_OFFSET)
        self.assertEqual(test_player_img.shape,
                         (config.PLAYER_HEIGHT, config.PLAYER_WIDTH, 3))
        self.assertIsInstance(test_player_img, ndarray)
