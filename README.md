
# 🪖 Helmet Detection with YOLOv8 + Streamlit

![Helmet Detection Banner](https://img.shields.io/badge/YOLOv8-Helmet%20Detection-blue?style=for-the-badge&logo=python)  
Real-time object detection for **safety helmets** using Ultralytics **YOLOv8** and a simple **Streamlit** web app.

---

## 📸 Demo

![Helmet Demo](https://github.com/your-username/your-repo-name/assets/your-demo.gif)  
> Detect helmets (with/without) in images and videos using deep learning 🔍

---

## 🚀 Features

✅ Built on [Ultralytics YOLOv8](https://docs.ultralytics.com/)  
✅ Detects `with_helmet` and `without_helmet`  
✅ Works with images and videos  
✅ Interactive web interface with [Streamlit](https://streamlit.io)  
✅ GPU acceleration for fast inference  
✅ Fully open-source 🔓

---

## 📁 Project Structure

```
HelmetApp/
├── app.py                   # Streamlit web app
├── data.yaml                # Dataset config
├── runs/                    # YOLO training results
│   └── detect/helmet_exp5/weights/best.pt
├── requirements.txt         # Python dependencies
└── README.md                # You are here
```

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/your-username/helmet-detection-yolov8-streamlit
cd helmet-detection-yolov8-streamlit

# Create environment (optional but recommended)
conda create -n yolo python=3.9 -y
conda activate yolo

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser at: [http://localhost:8501](http://localhost:8501)

---

## 🧠 Model Info

- **Model:** `yolov8s.pt` fine-tuned on helmet dataset (764 images)
- **Classes:** `with_helmet`, `without_helmet`
- **Framework:** PyTorch (via Ultralytics)

---

## 📦 Inference Example

```bash
# Image or video prediction via CLI
yolo predict model=runs/detect/helmet_exp5/weights/best.pt source=your_video.mp4
```
<img width="1190" height="512" alt="image" src="https://github.com/user-attachments/assets/6ec363b7-b7fe-4597-91ff-bf645a8a9b23" />


---

## 📊 Results

| Metric     | Score |
|------------|-------|
| mAP@0.5    | 0.768 |
| Precision  | 0.745 |
| Recall     | 0.755 |

---

Created with 💙 by Visara De Alwis
