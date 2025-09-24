import cv2
import numpy as np
import streamlit as st

# Sketch function
def sketch(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(gray_blur, 10, 70)
    _, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    return mask

# Streamlit UI
st.title("🎨 Real-time Sketch Filter with OpenCV + Streamlit")
st.write("Press **Stop** in the top-right corner to quit.")

# Start video stream
run = st.checkbox("Start Webcam")

FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    if not ret:
        st.write("Failed to grab frame")
        break
    # Apply sketch effect
    sketch_frame = sketch(frame)
    # Convert to RGB for streamlit
    sketch_frame_rgb = cv2.cvtColor(sketch_frame, cv2.COLOR_GRAY2RGB)
    FRAME_WINDOW.image(sketch_frame_rgb)

camera.release()
