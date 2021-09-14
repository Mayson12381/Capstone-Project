import tkinter as tk
from tkinter import *
from functools import partial
import threading
import cv2
import config
from firebase_authentication import login_user


class Login(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        def validateLogin(username, password):
            print("username entered :", username.get())
            print("password entered :", password.get())
            return

        #username label and text entry box
        usernameLabel = Label(self, text="User Name").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(self, textvariable=username).grid(row=0,
                                                                column=1)

        #password label and password entry box
        passwordLabel = Label(self, text="Password").grid(row=1, column=0)
        password = StringVar()
        passwordEntry = Entry(self, textvariable=password,
                              show='*').grid(row=1, column=1)

        validateLogin = partial(validateLogin, username, password)

        #login button
        loginButton = Button(self, text="Login",
                             command=validateLogin).grid(row=4, column=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)


class MainFrame(tk.Frame):
    def __init__(self, parent, getPlayersFull, getPlayersSingle, show_image_with_detections):
        self.getPlayersFull = getPlayersFull
        self.getPlayersSingle = getPlayersSingle
        self.show_image_with_detections = show_image_with_detections
        self.status_login = StringVar()
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
        Button(self, text='Configure',
               command=self.configure_detection).grid(row=3,
                                                      column=1,
                                                      pady=(10, 10),
                                                      padx=75,
                                                      sticky="ew")
        Button(self,
               text='Test Detection',
               command=self.test_detection).grid(row=4,
                                                                   column=1,
                                                                   pady=(10,
                                                                         20),
                                                                   padx=75,
                                                                   sticky="ew")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def configure_detection(self):
        image = self.getPlayersFull(config.TEST_IMAGE_PATH,
                                    config.PLAYER_X_OFFSET,
                                    config.PLAYER_HEIGTH,
                                    config.PLAYER_Y_OFFSET)
        cv2.imshow("Configure", image)

    def test_detection(self):
        thread_thread = threading.Thread(
            target=self.show_image_with_detections,
            args=(self.getPlayersSingle, self.getPlayersFull))
        thread_thread.setDaemon(True)
        thread_thread.start()

    def login(self):
        user_authenticated = login_user()
        config.is_user_logged_in = user_authenticated
        self.status_login.set("Online")