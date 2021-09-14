import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
import os
import cv2
import numpy as np
import config

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def get_model():
    model = tf.saved_model.load(config.SAVED_MODEL_PATH)
    return model


def get_player_data_from_image(image, get_players_seperated):
    (player1, player2, player3, player4, player5) = get_players_seperated(
        config.TEST_IMAGE_PATH, config.PLAYER_X_OFFSET, config.PLAYER_HEIGTH,
        config.PLAYER_Y_OFFSET)
    detections1, categories = get_image_detections(player1)
    detections2, _ = get_image_detections(player2)
    detections3, _ = get_image_detections(player3)
    detections4, _ = get_image_detections(player4)
    detections5, _ = get_image_detections(player5)

    player_data = {
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
    print(detections1['detection_classes'], detections1['detection_scores'])
    for index, detections in enumerate(
        [detections1, detections2, detections3, detections4, detections5]):
        for detection_class, detection_score in zip(
                detections['detection_classes'],
                detections['detection_scores']):
            if detection_score > config.MIN_CONF_THRESH:
                if detection_class in [
                        9
                ] and player_data['player' + str(index + 1)]['weapon'] not in [
                        'AK-47', 'M4', 'AWP'
                ]:
                    player_data[
                        'player' +
                        str(index +
                            1)]['weapon'] = categories[detection_class]['name']
                if detection_class in [1, 2, 3]:
                    player_data[
                        'player' +
                        str(index +
                            1)]['weapon'] = categories[detection_class]['name']
                if detection_class in [4]:
                    player_data['player' + str(index + 1)]['health_status'] = 0
                if detection_class in [5, 6, 7, 8]:
                    player_data['player' + str(index + 1)]['nades'].append(
                        categories[detection_class]['name'])
                if detection_class in [10, 11]:
                    player_data[
                        'player' +
                        str(index +
                            1)]['kevlar'] = categories[detection_class]['name']
    return (player_data)


def show_image_with_detections(get_players_seperated, get_players_full):
    (player1, player2, player3, player4, player5) = get_players_seperated(
        config.TEST_IMAGE_PATH, config.PLAYER_X_OFFSET, config.PLAYER_HEIGTH,
        config.PLAYER_Y_OFFSET)
    detections1, categories = get_image_detections(player1)
    detections2, _ = get_image_detections(player2)
    detections3, _ = get_image_detections(player3)
    detections4, _ = get_image_detections(player4)
    detections5, _ = get_image_detections(player5)

    full_image = get_players_full(config.TEST_IMAGE_PATH,
                                  config.PLAYER_X_OFFSET, config.PLAYER_HEIGTH,
                                  config.PLAYER_Y_OFFSET)
    image = apply_detections_to_full_image(
        full_image,
        [detections1, detections2, detections3, detections4, detections5],
        categories)
    cv2.imshow("Detection", image)
    cv2.waitKey(0)


def apply_detections_to_full_image(image, detections_list, categories):
    adder = 0
    for index, detection in enumerate(detections_list):
        for index2, (box, score) in enumerate(
                zip(detection['detection_boxes'],
                    detection['detection_scores'])):
            detections_list[index]['detection_boxes'][index2][0] = (
                round(box[0] * 53.0) + adder) / image.shape[0]
            detections_list[index]['detection_boxes'][index2][2] = (
                round(box[2] * 53.0) + adder) / image.shape[0]
        adder += image.shape[0] / 5

    return viz_utils.visualize_boxes_and_labels_on_image_array(
        image.copy(),
        np.concatenate((detections_list[0]['detection_boxes'],
                        detections_list[1]['detection_boxes'],
                        detections_list[2]['detection_boxes'],
                        detections_list[3]['detection_boxes'],
                        detections_list[4]['detection_boxes'])),
        np.concatenate((detections_list[0]['detection_classes'],
                        detections_list[1]['detection_classes'],
                        detections_list[2]['detection_classes'],
                        detections_list[3]['detection_classes'],
                        detections_list[4]['detection_classes'])),
        np.concatenate((detections_list[0]['detection_scores'],
                        detections_list[1]['detection_scores'],
                        detections_list[2]['detection_scores'],
                        detections_list[3]['detection_scores'],
                        detections_list[4]['detection_scores'])),
        categories,
        use_normalized_coordinates=True,
        max_boxes_to_draw=20,
        min_score_thresh=config.MIN_CONF_THRESH,
        agnostic_mode=False,
        line_thickness=1)


def get_detection(model, image):
    category_index = label_map_util.create_category_index_from_labelmap(
        config.LABELS_PATH, use_display_name=True)
    image_np = image
    input_tensor = tf.convert_to_tensor(image_np)
    input_tensor = input_tensor[tf.newaxis, ...]
    detections = model(input_tensor)
    num_detections = int(detections.pop('num_detections'))
    detections = {
        key: value[0, :num_detections].numpy()
        for key, value in detections.items()
    }
    detections['num_detections'] = num_detections
    detections['detection_classes'] = detections['detection_classes'].astype(
        np.int64)
    image_np_with_detections = image_np.copy()
    return detections, category_index


def get_image_detections(image):
    return get_detection(config.model,
                         np.array(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
