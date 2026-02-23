import streamlit as st
from PIL import Image
import random

st.title("Crop Theft & Animal Intrusion Detection System")

st.write("Upload an image to simulate intrusion detection")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Simulated detection logic
    detection = random.choice(["Human", "Animal"])

    if detection == "Human":
        st.success("Human Detected!")
        st.write("Alert: SMS Sent to Farmer")
        st.write("Alarm Activated")
    else:
        st.warning("Animal Detected")
        st.write("Monitoring Situation")
