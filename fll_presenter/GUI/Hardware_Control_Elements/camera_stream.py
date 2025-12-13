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


def get_camera_frame(cam_index, length, height):
    """Function to capture a frame from the specified camera index, returns a PhotoImage type"""
    # NOTE: Assuming VID_STREAMS and cv2/Image/ImageTk are imported/available globally in that scope.

    # 1. Capture the video frame by frame
    _, frame = VID_STREAMS[cam_index].read()

    # 2. Convert image from one color space to other (OpenCV to format expected by PIL)
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    # 3. Capture the latest frame and transform to PIL Image
    captured_image = Image.fromarray(opencv_image)

    # 4. CRITICAL FIX: Resize the PIL Image using the required dimensions (length, height)
    # The Image object (captured_image) has the .resize() method.
    resized_image = captured_image.resize((length, height), Image.LANCZOS)

    # 5. Convert the resized PIL image to PhotoImage (the final Tkinter format)
    photo_image = ImageTk.PhotoImage(image=resized_image)

    # 6. Return the PhotoImage
    return photo_image


print("Starting camera test")
print(get_avalible_cameras())
