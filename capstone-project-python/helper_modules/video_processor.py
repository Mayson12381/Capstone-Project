import cv2
from numpy import ndarray

def read_image_from_video_stream(camera_id: int) -> ndarray:
    """
    Reads an image from the video stream.
    :return: The image read from the video stream.
    """
    cap = cv2.VideoCapture(camera_id)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    width = 1920
    height = 1080
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    if (cap.isOpened() == False):
        print("Error opening video stream or file")
    ret, frame = cap.read()
    cap.release()
    return frame
