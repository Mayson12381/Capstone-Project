import cv2
import numpy as np
import os
import sys

ROOT_DIRECTORY_PATH = sys.path[0]


def getFrame(sec, src, img_out):
    vidcap = cv2.VideoCapture(src)
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        baseX = 350
        playerHeight = 43

        player1 = image[baseX:baseX + playerHeight, 0:450]
        player2 = image[baseX + playerHeight:baseX + 2 * playerHeight, 0:450]
        player3 = image[baseX + 2 * playerHeight:baseX + 3 * playerHeight, 0:450]
        player4 = image[baseX + 3 * playerHeight:baseX + 4 * playerHeight, 0:450]
        player5 = image[baseX + 4 * playerHeight:baseX + 5 * playerHeight, 0:450]
        cv2.imwrite(img_out + '_player-1' + '.jpg', player1)
        cv2.imwrite(img_out + '_player-2' + '.jpg', player2)
        cv2.imwrite(img_out + '_player-3' + '.jpg', player3)
        cv2.imwrite(img_out + '_player-4' + '.jpg', player4)
        cv2.imwrite(img_out + '_player-5' + '.jpg', player5)
    return hasFrames


def create_frame(src, dst):
    sec = 0
    frameRate = 1  # it will capture image in each 1 second
    count = 1
    img_out = dst + '_' + str(count)
    success = getFrame(sec, src, img_out)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        img_out = dst + '_' + str(count)
        success = getFrame(sec, src, img_out)


for mp4name in os.listdir('videos'):
    create_frame(ROOT_DIRECTORY_PATH + '/videos/' + mp4name,
                 ROOT_DIRECTORY_PATH + '/dataset/' + mp4name.split('.mp4')[0])
