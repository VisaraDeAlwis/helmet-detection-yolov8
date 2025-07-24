import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np
import tempfile

# Load YOLOv8 model
model = YOLO("runs/detect/helmet_exp8/weights/best.pt")

st.title("🪖 Helmet Detection using YOLOv8")
st.markdown("Upload an image or video to detect helmets.")

option = st.radio("Choose input type:", ["Image", "Video"])

if option == "Image":
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        image = Image.open(uploaded_image).convert("RGB")
        results = model.predict(source=np.array(image), save=False)
        result_img = results[0].plot()
        st.image(result_img, caption="Prediction", use_container_width=True)

elif option == "Video":
    uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        cap = cv2.VideoCapture(tfile.name)

        stframe = st.empty()
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model.predict(source=frame, save=False)
            annotated_frame = results[0].plot()
            stframe.image(annotated_frame, channels="BGR", use_container_width=True)
        cap.release()
