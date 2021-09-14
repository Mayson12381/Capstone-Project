import multiprocessing
import os
import threading
import time
import tkinter as tk
import cv2

import numpy as np

import config
from firebase_functions import update_game_data, update_last_online, init_firebase
from detections import get_player_data_from_image
from frames import MainFrame
from image_processor import getPlayerImagesLeftFull, getPlayerImagesLeftSingle, getPlayerImagesRightFull, getPlayerImagesRightSingle

from object_detection.utils import visualization_utils as viz_utils

from detections import show_image_with_detections, get_model


def main_loop():
    while 1:
        if config.is_user_logged_in:
            time.sleep(1)
            if config.is_game_data_requested:
                config.is_game_data_requested = False
                player_data = get_player_data_from_image(
                    cv2.imread(config.TEST_IMAGE_PATH),
                    getPlayerImagesRightSingle)
                update_game_data(player_data)
            update_last_online()


def init_TKInter():
    root_frame = tk.Tk()
    MainFrame(root_frame, getPlayerImagesRightFull, getPlayerImagesRightSingle,
              show_image_with_detections).grid(sticky="ew")

    root_frame.grid_rowconfigure(0, weight=1)
    root_frame.grid_columnconfigure(0, weight=1)
    root_frame.resizable(0, 0)
    root_frame.mainloop()


if __name__ == "__main__":
    config.model = get_model()
    init_firebase()

    loop_thread = threading.Thread(target=main_loop, args=())
    loop_thread.setDaemon(True)
    loop_thread.start()

    get_player_data_from_image(cv2.imread(config.TEST_IMAGE_PATH),
                             getPlayerImagesLeftSingle)

    init_TKInter()
