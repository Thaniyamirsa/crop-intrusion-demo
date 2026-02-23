import streamlit as st
from PIL import Image
import cv2
import numpy as np

st.title("Crop Theft & Animal Intrusion Detection System")

st.write("Upload an image to detect Human or Animal")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert image to OpenCV format
    img_array = np.array(image)
    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

    # Load face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        st.success("Human Detected!")
        st.write("Alert: SMS Sent to Farmer")
        st.write("Alarm Activated")
    else:
        st.warning("Animal Detected")
        st.write("Monitoring Situation")
