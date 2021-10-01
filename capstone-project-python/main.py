import threading
import time
import tkinter as tk

import cv2

import config
from data_detection.detections import (get_team_data_from_image, load_model,
                                       show_image_with_detections)
from data_detection.image_processor import (get_player_images_left,
                                            get_player_images_right,
                                            get_team_image_left,
                                            get_team_image_right)
from firebase_helpers.firebase_functions import (init_firebase,
                                                 update_game_data,
                                                 update_last_online)
from gui.tkinter_frames import MainFrame
from helper_modules.video_processor import read_image_from_video_stream


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
                    cv2.imread(config.TEST_IMAGE_PATH) if config.input_type == 'Image' else read_image_from_video_stream(config.camera_input_id),
                    get_player_images_left
                    if config.is_team_left else get_player_images_right)
                update_game_data(player_data)
            update_last_online()


def init_gui():
    """
    Initializes the GUI.
    :return: None
    """
    root_frame = tk.Tk()
    MainFrame(parent=root_frame,
              getPlayersFull=get_team_image_left
              if config.is_team_left else get_team_image_right,
              getPlayersSingle=get_player_images_left
              if config.is_team_left else get_player_images_right,
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
