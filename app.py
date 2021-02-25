import cv2
import streamlit as st
import face_recognition
import pandas as pd
import numpy as np

def check_webcam():
    webcam_dict = dict()
    camera_number=None
    for i in range(0, 5):
        cap = cv2.VideoCapture(i)
        is_camera = cap.isOpened()
        if is_camera:
            webcam_dict[f"index[{i}]"] = "VALID"
            cap.release()
            camera_number = i
        else:
            webcam_dict[f"index[{i}]"] = None

    return webcam_dict,camera_number

st.title('WebCam index validation check')
webcam_dict,camera_number = check_webcam()


st.write(webcam_dict)

if camera_number != None:
    # print(camera_number)
    st.write(camera_number)

# CONSTANTS
WEBCAMNUM = camera_number # from videocapture_index_check.py
# PATH_DATA = 'data/DB.csv'
# COLOR_DARK = (0, 0, 153)
# COLOR_WHITE = (255, 255, 255)
# COLS_INFO = ['name', 'description']
# COLS_ENCODE = [f'v{i}' for i in range(128)]

st.title("Webcam Face Recognition")
FRAME_WINDOW = st.image([])
button=st.button("capture")


def capture_face(video_capture):
    # got 3 frames to auto adjust webcam light
    for i in range(3):
        video_capture.read()

    while(True):
        ret, frame = video_capture.read()
        FRAME_WINDOW.image(frame[:, :, ::-1])
        # face detection
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        video_capture.release()
        rgb_frame = frame[:, :, ::-1]
        return rgb_frame


if __name__ == "__main__":
    c=True
    while(c):
        video_capture = cv2.VideoCapture(WEBCAMNUM)
        frame = capture_face(video_capture)
        FRAME_WINDOW.image(frame)

        if button:
            c=False
    st.write('contunue......')