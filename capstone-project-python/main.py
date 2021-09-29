import threading
import time
import tkinter as tk

import cv2
from data_detection.detections import (load_model, get_team_data_from_image,
                                       show_image_with_detections)

import config
from data_detection.image_processor import (getPlayerImagesLeftFull,
                                            getPlayerImagesLeftSeperated,
                                            getPlayerImagesRightFull,
                                            getPlayerImagesRightSeperated)
from firebase_helpers.firebase_functions import (init_firebase,
                                                 update_game_data,
                                                 update_last_online)
from gui.tkinter_frames import MainFrame


def main_loop():
    """
    Main loop of the program.
    :return: None
    """
    while 1:
        if config.is_user_logged_in:
            time.sleep(1)
            if config.is_game_data_requested:
                config.is_game_data_requested = False
                player_data = get_team_data_from_image(
                    cv2.imread(config.TEST_IMAGE_PATH),
                    getPlayerImagesLeftSeperated
                    if config.is_team_left else getPlayerImagesRightSeperated)
                update_game_data(player_data)
            update_last_online()


def init_gui():
    """
    Initializes the GUI.
    :return: None
    """
    root_frame = tk.Tk()
    MainFrame(parent=root_frame,
              getPlayersFull=getPlayerImagesLeftFull
              if config.is_team_left else getPlayerImagesRightFull,
              getPlayersSingle=getPlayerImagesLeftSeperated
              if config.is_team_left else getPlayerImagesRightSeperated,
              show_image_with_detections=show_image_with_detections).grid(
                  sticky="ew")

    root_frame.grid_rowconfigure(0, weight=1)
    root_frame.grid_columnconfigure(0, weight=1)
    root_frame.resizable(0, 0)
    root_frame.mainloop()


if __name__ == "__main__":
    config.model = load_model()
    init_firebase()

    loop_thread = threading.Thread(target=main_loop, args=())
    loop_thread.setDaemon(True)
    loop_thread.start()

    init_gui()
