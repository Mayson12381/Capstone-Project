# py main.py --image test-screen_1.png

import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--video", required = True, help = "Path to the video")
args = vars(ap.parse_args())

vidcap = cv2.VideoCapture(args["video"])
vidcap.set(cv2.CAP_PROP_POS_MSEC, 0 * 1000)
_, image = vidcap.read()

baseX = 350
playerHeight = 43

player1 = image[baseX:baseX + playerHeight, 0:450]
player2 = image[baseX + playerHeight:baseX + 2 * playerHeight, 0:450]
player3 = image[baseX + 2 * playerHeight:baseX + 3 * playerHeight, 0:450]
player4 = image[baseX + 3 * playerHeight:baseX + 4 * playerHeight, 0:450]
player5 = image[baseX + 4 * playerHeight:baseX + 5 * playerHeight, 0:450]

cv2.imshow("player1", player1)
cv2.imshow("player2", player2)
cv2.imshow("player3", player3)
cv2.imshow("player4", player4)
cv2.imshow("player5", player5)
cv2.waitKey(0)