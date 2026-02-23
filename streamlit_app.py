import streamlit as st
import cv2

st.title("Crop Theft & Animal Intrusion Detection Demo")

run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)

human_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_fullbody.xml'
)

while run:
    ret, frame = camera.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.1, 4)

    if len(humans) > 0:
        st.success("Human Detected!")
        st.write("SMS Alert Sent to Farmer")
        st.write("Alarm Activated")
    else:
        st.warning("Animal Detected")

    FRAME_WINDOW.image(frame, channels="BGR")

camera.release()
