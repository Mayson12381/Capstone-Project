import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
import os
import cv2
import numpy as np
import config
from typing import List, Callable, Dict

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# MARK: - Public functions


def load_model() -> tf.keras.models.Model:
    """
    Loads the model from the config file
    :return: the model
    """
    model = tf.saved_model.load(config.SAVED_MODEL_PATH)
    return model


def get_team_data_from_image(full_img: List,
                             get_players_seperated_func: Callable) -> Dict:
    """
    Gets the team data from the image
    :param full_img: the fullscreen image
    :param get_players_seperated_func: the function to get the 5 player images seperated
    :return: the team data
    """
    detections, categories = _get_team_detections_and_categories(
        full_img, get_players_seperated_func)
    return _get_team_data_from_detections(detections, categories)


def show_image_with_detections(full_img: List,
                               get_players_seperated_func: Callable,
                               get_team_img_func: Callable) -> None:
    """
    Shows the image with the detections
    :param full_img: the fullscreen image
    :param get_players_seperated_func: the function to get the 5 player images seperated
    :param get_team_img_func: the function to get the team image
    :return: None
    """
    team_detections, detection_categories = _get_team_detections_and_categories(
        full_img, get_players_seperated_func)

    team_img = get_team_img_func(full_img, config.PLAYER_X_OFFSET,
                                 config.PLAYER_HEIGTH, config.PLAYER_Y_OFFSET)
    team_img_with_detections = _apply_detections_to_team_image(
        team_img, team_detections, detection_categories)
    cv2.imshow("Detection", team_img_with_detections)
    cv2.waitKey(0)


# MARK: - Private functions


def _get_team_detections_and_categories(
        full_img: List, get_players_seperated_func: Callable) -> (List, List):
    """
    Gets the team detections and categories
    :param full_img: the fullscreen image
    :param get_players_seperated_func: the function to get the 5 player images seperated
    :return: player detections and categories
    """
    (player1_img, player2_img, player3_img, player4_img,
     player5_img) = get_players_seperated_func(full_img,
                                               config.PLAYER_X_OFFSET,
                                               config.PLAYER_HEIGTH,
                                               config.PLAYER_Y_OFFSET)
    player1_det, categories = _get_player_detections(player1_img)
    player2_det, _ = _get_player_detections(player2_img)
    player3_det, _ = _get_player_detections(player3_img)
    player4_det, _ = _get_player_detections(player4_img)
    player5_det, _ = _get_player_detections(player5_img)

    return [player1_det, player2_det, player3_det, player4_det,
            player5_det], categories


def _initialize_empty_team_data() -> Dict:
    """
    Initializes the empty player data
    :return: the empty player data
    """
    return {
        'player1': {
            'health_status': 1,
            'nades': [],
            'kevlar': None
        },
        'player2': {
            'health_status': 1,
            'nades': [],
            'kevlar': None
        },
        'player3': {
            'health_status': 1,
            'nades': [],
            'kevlar': None
        },
        'player4': {
            'health_status': 1,
            'nades': [],
            'kevlar': None
        },
        'player5': {
            'health_status': 1,
            'nades': [],
            'kevlar': None
        },
    }


def _get_team_data_from_detections(team_detections: List,
                                   detection_categories: List) -> Dict:
    """
    Gets the team data from the detections
    :param team_detections: the teams detections
    :param detection_categories: the detection categories
    :return: the team data
    """
    team_data = _initialize_empty_team_data()
    for index, team_detections in enumerate(team_detections):
        for detection_class, detection_score in zip(
                team_detections['detection_classes'],
                team_detections['detection_scores']):
            if detection_score > config.MIN_CONF_THRESH:
                if detection_class in [
                        9
                ] and team_data['player' + str(index + 1)]['weapon'] not in [
                        'AK-47', 'M4', 'AWP'
                ]:
                    team_data['player' +
                                str(index +
                                    1)]['weapon'] = detection_categories[
                                        detection_class]['name']
                if detection_class in [1, 2, 3]:
                    team_data['player' +
                                str(index +
                                    1)]['weapon'] = detection_categories[
                                        detection_class]['name']
                if detection_class in [4]:
                    team_data['player' + str(index + 1)]['health_status'] = 0
                if detection_class in [5, 6, 7, 8]:
                    team_data['player' + str(index + 1)]['nades'].append(
                        detection_categories[detection_class]['name'])
                if detection_class in [10, 11]:
                    team_data['player' +
                                str(index +
                                    1)]['kevlar'] = detection_categories[
                                        detection_class]['name']
    return team_data


def _apply_detections_to_team_image(team_img: List, team_detections: List,
                                    detection_categories: List) -> list:
    """
    Applies the detections to the team image
    :param team_img: the team image
    :param team_detections: the team detections
    :param detection_categories: the detection categories
    :return: the team image with the detections
    """
    adder = 0
    for index, detection in enumerate(team_detections):
        for index2, (box, score) in enumerate(
                zip(detection['detection_boxes'],
                    detection['detection_scores'])):
            team_detections[index]['detection_boxes'][index2][0] = (
                round(box[0] * 53.0) + adder) / team_img.shape[0]
            team_detections[index]['detection_boxes'][index2][2] = (
                round(box[2] * 53.0) + adder) / team_img.shape[0]
        adder += team_img.shape[0] / 5
    return viz_utils.visualize_boxes_and_labels_on_image_array(
        team_img.copy(),
        np.concatenate((team_detections[0]['detection_boxes'],
                        team_detections[1]['detection_boxes'],
                        team_detections[2]['detection_boxes'],
                        team_detections[3]['detection_boxes'],
                        team_detections[4]['detection_boxes'])),
        np.concatenate((team_detections[0]['detection_classes'],
                        team_detections[1]['detection_classes'],
                        team_detections[2]['detection_classes'],
                        team_detections[3]['detection_classes'],
                        team_detections[4]['detection_classes'])),
        np.concatenate((team_detections[0]['detection_scores'],
                        team_detections[1]['detection_scores'],
                        team_detections[2]['detection_scores'],
                        team_detections[3]['detection_scores'],
                        team_detections[4]['detection_scores'])),
        detection_categories,
        use_normalized_coordinates=True,
        max_boxes_to_draw=20,
        min_score_thresh=config.MIN_CONF_THRESH,
        agnostic_mode=False,
        line_thickness=1)


def _get_player_detections(player_img: List) -> (List, List):
    """
    Gets the player detections
    :param player_img: the player image
    :return: the player detections and detection categories
    """
    img = np.array(cv2.cvtColor(player_img, cv2.COLOR_BGR2RGB))
    model = config.model
    detection_categories = label_map_util.create_category_index_from_labelmap(
        config.LABELS_PATH, use_display_name=True)
    image_np = img
    input_tensor = tf.convert_to_tensor(image_np)
    input_tensor = input_tensor[tf.newaxis, ...]
    player_detections = model(input_tensor)
    num_detections = int(player_detections.pop('num_detections'))
    player_detections = {
        key: value[0, :num_detections].numpy()
        for key, value in player_detections.items()
    }
    player_detections['num_detections'] = num_detections
    player_detections['detection_classes'] = player_detections[
        'detection_classes'].astype(np.int64)
    image_np_with_detections = image_np.copy()
    return player_detections, detection_categories
