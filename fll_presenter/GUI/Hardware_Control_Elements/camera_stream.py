import cv2
import PIL
from PIL import Image, ImageTk
from tkinter import PhotoImage
from cv2_enumerate_cameras import enumerate_cameras

VID_STREAMS = []


def get_avalible_cameras():
    """Returns a dictionary of available camera indices connected to the system."""
    cams = {}
    for camera_info in enumerate_cameras(cv2.CAP_MSMF):
        cams[camera_info.index] = camera_info.name
    return cams


def init_cameras(cam_indicies):
    for i in cam_indicies:
        VID_STREAMS.append(cv2.VideoCapture(i))


def get_camera_frame(cam_index):
    """Function to capture a frame from the specified camera index, returns a PhotoImage type"""
    # Capture the video frame by frame
    _, frame = VID_STREAMS[cam_index].read()

    # Convert image from one color space to other
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    # Capture the latest frame and transform to image
    captured_image = Image.fromarray(opencv_image)

    # Convert captured image to photoimage
    photo_image = ImageTk.PhotoImage(image=captured_image)

    return photo_image


print("Starting camera test")
print(get_avalible_cameras())
