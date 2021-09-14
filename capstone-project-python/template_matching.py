import cv2
import numpy as np
from matplotlib import pyplot as plt
from image_processor import getPlayerImagesRightSingle
import config


def upscale_with_aspect_ratio(img, upscale_factor):
    """
    Upscales image with aspect ratio.
    :param img: image to upscale
    :param upscale_factor: factor to upscale
    :return: upscaled image
    """
    height, width = img.shape[:2]
    new_height = int(height * upscale_factor)
    new_width = int(width * upscale_factor)
    return cv2.resize(img, (new_width, new_height))


def flip_image_horizontally(img):
    """
    Flips image horizontally.
    :param img: image to flip
    :return: flipped image
    """
    return cv2.flip(img, 1)


_, _, img_rgb, _, _ = getPlayerImagesRightSingle('test-screen_7.jpg',
                                                       config.PLAYER_X_OFFSET,
                                                       config.PLAYER_HEIGTH,
                                                       config.PLAYER_Y_OFFSET)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('he_template.png', 0)
template = flip_image_horizontally(template)
template = upscale_with_aspect_ratio(template, 0.5)

height, width = template.shape[::]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
plt.imshow(res, cmap='gray')

threshold = 0.75  #For TM_CCOEFF_NORMED, larger values = good fit.

loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + width, pt[1] + height), (255, 0, 0), 1)

print(len(loc))

cv2.imshow("Matched image", img_rgb)
cv2.imshow("template", template)
cv2.waitKey()
cv2.destroyAllWindows()