import tkinter as tk
from tkinter import *
from functools import partial
import threading
import cv2
import config
from firebase_helpers.firebase_authentication import login_user


class MainFrame(tk.Frame):
    def __init__(self, parent, getPlayersFull, getPlayersSingle,
                 show_image_with_detections):
        self.getPlayersFull = getPlayersFull
        self.getPlayersSingle = getPlayersSingle
        self.show_image_with_detections = show_image_with_detections
        self.status_login = StringVar()
        self.teamside = StringVar()
        self.input_type = StringVar()
        tk.Frame.__init__(self, parent)

        parent.title("Companion")
        Label(self, textvariable=self.status_login).grid(row=1,
                                                         column=1,
                                                         pady=(20, 10),
                                                         padx=75)
        self.status_login.set("Offline")
        Button(self, text='Login', command=self.login).grid(row=2,
                                                            column=1,
                                                            pady=(10, 10),
                                                            padx=75,
                                                            sticky="ew")
        Button(self,
               textvariable=self.teamside,
               command=self.switch_teamside).grid(row=3,
                                        column=1,
                                        pady=(10, 10),
                                        padx=75,
                                        sticky="ew")
        self.teamside.set('Teamside - left' if config.is_team_left else 'Teamside - right')
        Button(self,
               textvariable=self.input_type,
               command=self.switch_input_type).grid(row=4,
                                        column=1,
                                        pady=(10, 10),
                                        padx=75,
                                        sticky="ew")
        self.input_type.set('Input type - ' + config.input_type)
        Button(self, text='Test Detection',
               command=self.test_detection).grid(row=5,
                                                 column=1,
                                                 pady=(10, 20),
                                                 padx=75,
                                                 sticky="ew")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def switch_teamside(self):
        config.is_team_left = not config.is_team_left
        self.teamside.set('Teamside - left' if config.is_team_left else 'Teamside - right')

    def switch_input_type(self):
        config.input_type = 'Stream' if config.input_type == 'Image' else 'Image'
        self.input_type.set('Input type - ' + config.input_type)

    def test_detection(self):
        thread_thread = threading.Thread(
            target=self.show_image_with_detections,
            args=(cv2.imread(config.TEST_IMAGE_PATH), self.getPlayersSingle, self.getPlayersFull))
        thread_thread.setDaemon(True)
        thread_thread.start()

    def login(self):
        user_authenticated = login_user('dev@capstone.com', 'Passw0rd!')
        config.is_user_logged_in = user_authenticated
        if user_authenticated:
            self.status_login.set("Online")
