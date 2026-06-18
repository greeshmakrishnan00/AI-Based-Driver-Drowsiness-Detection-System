# 🚗 Driver Drowsiness Detection System Using AI

## 📌 Overview
This project is a real-time AI-based Driver Drowsiness Detection System developed using Python, OpenCV, and MediaPipe. It detects a driver's eye state through webcam input and identifies drowsiness using Eye Aspect Ratio (EAR). If the driver’s eyes remain closed for more than 3 seconds, an alarm is triggered to alert the driver and prevent possible accidents.

---

## 🎯 Objective
To enhance road safety by detecting driver fatigue in real-time using computer vision and providing immediate alerts when drowsiness is detected.

---

## ⚙️ Features
- Real-time face and eye detection using webcam  
- AI-based facial landmark detection using MediaPipe Face Mesh  
- Eye Aspect Ratio (EAR) calculation for drowsiness detection  
- Detects continuous eye closure for more than 3 seconds  
- Automatic alarm alert system  
- Live video processing using OpenCV  

---

## 🛠️ Tech Stack
- Python  
- OpenCV  
- MediaPipe  
- NumPy  
- Threading  
- Winsound (Windows built-in audio alert system)  

---

## 📂 Project Structure
Driver_Drowsiness_Detection_System/
│
├── Driver_Drowsiness_Detection.py
├── README.md

---

## 📦 Installation

Install required dependencies:

pip install opencv-python mediapipe numpy

---

## ▶️ How to Run

Run the Python file:

python Driver_Drowsiness_Detection.py

Press ESC to exit the application.

---

## 🧠 How It Works
1. Webcam captures live video  
2. MediaPipe Face Mesh detects facial landmarks  
3. Eye landmarks are extracted  
4. Eye Aspect Ratio (EAR) is calculated  
5. If eyes remain closed for more than 3 seconds → drowsiness detected  
6. Alarm is triggered immediately  

---

## 🔊 Alert System
- Uses `winsound.Beep()` for alarm sound (Windows OS)  
- Alarm activates only when eyes are continuously closed  
- Automatically stops when eyes are open  

---

## 📸 Output
- Live webcam feed  
- Eye landmark visualization  
- EAR value display  
- “DROWSINESS ALERT” warning message  

---

## 🚀 Future Improvements
- Yawn detection system  
- Head pose estimation  
- Mobile notification alerts  
- Deep learning-based fatigue detection  
- Night driving support using IR camera  

---

## ⚠️ Limitations
- Works best in good lighting conditions  
- Requires frontal face visibility  
- Accuracy depends on webcam quality  

---

## 👨‍💻 Author
Greeshma R Krishnan  
AI & Data Science Enthusiast  
Machine Learning | Deep Learning | Computer Vision  

---

## ⭐ Support
If you like this project, please give a ⭐ to this repository.
