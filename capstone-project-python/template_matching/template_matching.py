import cv2
import numpy as np
from matplotlib import pyplot as plt
from data_detection.image_processor import get_player_images_right, get_player_images_left
import config
import matplotlib.pyplot as plt


# MARK: - Private methods


def _flip_image_horizontally(img: np.ndarray) -> np.ndarray:
    """
    Flips image horizontally.
    :param img: image to flip
    :return: flipped image
    """
    return cv2.flip(img, 1)


def _scale_image_horizontally(img: np.ndarray,
                              scale_factor: int) -> np.ndarray:
    """
    Scales image horizontally.
    :param img: image to scale
    :param scale_factor: factor to scale
    :return: scaled image
    """
    return cv2.resize(img, None, fx=scale_factor, fy=1)


def _scale_image_vertically(img: np.ndarray, scale_factor: int) -> np.ndarray:
    """
    Scales image vertically.
    :param img: image to scale
    :param scale_factor: factor to scale
    :return: scaled image
    """
    return cv2.resize(img, None, fx=1, fy=scale_factor)


def _black_out_image_except_roi(img: np.ndarray, roi_x: int, roi_y: int,
                                roi_width: int, roi_height: int) -> np.ndarray:
    """
    Black out image except ROI.
    :param img: image to black out
    :param roi_x: x coordinate of ROI
    :param roi_y: y coordinate of ROI
    :param roi_width: width of ROI
    :param roi_height: height of ROI
    :return: blacked out image
    """
    black_out_image = np.zeros(img.shape, np.uint8)
    black_out_image[roi_y:roi_y + roi_height,
                    roi_x:roi_x + roi_width] = img[roi_y:roi_y + roi_height,
                                                   roi_x:roi_x + roi_width]
    return black_out_image


def _black_out_image_except_rgb_threshold(img: np.ndarray, threshold: int):
    """
    Black out image except pixels with rgb values varying more than a certain threshold.
    :param img: image to black out
    :param threshold: threshold to black out
    :return: blacked out image
    """
    black_out_image = np.zeros(img.shape, np.uint8)
    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            if (_max_diff([img[i][j][0], img[i][j][1], img[i][j][2]]) <=
                    threshold):
                black_out_image[i][j] = img[i][j]
    return black_out_image


def _max_diff(numbers: list):
    """
    Returns the maximum difference between a list of numbers.
    :param numbers: list of numbers
    :return: maximum difference between a list of numbers
    """
    return max(numbers) - min(numbers)


def _how_likely_is_player_dead(img: np.ndarray, player: np.ndarray) -> float:
    if config.is_team_left:
        img_dead = _black_out_image_except_roi(img, 0, 0, 80, player.shape[0])
    else:
        img_dead = _black_out_image_except_roi(img, player.shape[1] - 80, 0,
                                               player.shape[1],
                                               player.shape[0])

    template = cv2.imread('./templates/dead_template.png', 0)
    template = _scale_image_horizontally(template,
                                         config.DEAD_HORIZONTAL_SCALE_FACTOR)
    template = _scale_image_vertically(template,
                                       config.DEAD_VERTICAL_SCALE_FACTOR)

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_dead, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.35
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(res)

    return maxVal if maxVal >= threshold else 0


def show_and_print_template_detections(image_path: str) -> None: # pragma: no cover
    """
    Main function.
    :param image_path: path to image
    :return: None
    """
    getSingleImages = get_player_images_left if config.is_team_left else get_player_images_right
    player1, player2, player3, player4, player5 = get_player_images_left(
        image_path, config.PLAYER_X_OFFSET, config.PLAYER_HEIGHT,
        config.PLAYER_Y_OFFSET)

    for index, player in enumerate(
        [player1, player2, player3, player4, player5]):
        img_gray = cv2.cvtColor(player, cv2.COLOR_BGR2GRAY)
        thresh_img = cv2.cvtColor(
            _black_out_image_except_rgb_threshold(player, 5),
            cv2.COLOR_BGR2GRAY)

        found_icons = {
            'weapon': {
                'name': None,
                'percentage': 0
            },
            'armor': {
                'name': None,
                'percentage': 0
            },
            'utility': [],
            'status': 1
        }

        isPlayerDead = _how_likely_is_player_dead(img_gray, player)
        print(isPlayerDead)
        if isPlayerDead:
            found_icons['status'] = 0
        else:
            if config.is_team_left:
                img_weapon = _black_out_image_except_roi(
                    thresh_img, player.shape[1] - 275, 0, player.shape[1],
                    player.shape[0])
            else:
                img_weapon = _black_out_image_except_roi(
                    thresh_img, 0, 0, 275, player.shape[0])

            for weapon in config.WEAPONS:
                template = cv2.imread(
                    './templates/' + weapon + '_template.png', 0)
                if not config.is_team_left:
                    template = _flip_image_horizontally(template)
                template = _scale_image_horizontally(
                    template, config.WEAPON_HORIZONTAL_SCALE_FACTOR)
                template = _scale_image_vertically(
                    template, config.WEAPON_VERTICAL_SCALE_FACTOR)

                w, h = template.shape[::-1]
                res = cv2.matchTemplate(img_weapon, template,
                                        cv2.TM_CCOEFF_NORMED)
                threshold = 0.60
                loc = np.where(res >= threshold)
                (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(res)

                if found_icons['weapon'][
                        'percentage'] < maxVal and maxVal > threshold:
                    found_icons['weapon']['name'] = weapon
                    found_icons['weapon']['percentage'] = np.round(maxVal, 2)
                    (startX, startY) = maxLoc
                    endX = startX + template.shape[1]
                    endY = startY + template.shape[0]
                    cv2.rectangle(player, (startX, startY), (endX, endY),
                                  (255, 0, 0), 3)
                    print(weapon, maxVal)

                if maxVal > 0.8:
                    break

            print('player', index, found_icons)

    cv2.imshow("_", player1)
    cv2.imshow("_1", player2)
    cv2.imshow("_2", player3)
    cv2.imshow("_3", player4)
    cv2.imshow("_4", player5)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__': # pragma: no cover
    show_and_print_template_detections(
        '../helper_modules/test_images/test-screen_7.jpg')
