# ✋ Hand Gesture Controlled Motor System

A real-time system that uses **computer vision and hand gesture recognition** to control motors wirelessly. This project integrates **OpenCV + MediaPipe + Embedded Systems (ESP32/STM32)** to translate human gestures into physical motor actions.

---

## 🚀 Features

* 🎯 Real-time hand tracking using MediaPipe
* 🖐️ Gesture-based control (forward, backward, stop, etc.)
* ⚡ Low-latency communication between PC and microcontroller
* 🔌 Works with ESP32 / STM32 motor control systems
* 📡 Wireless control (WiFi-based communication)

---

## 🧠 Tech Stack

### 👨‍💻 Computer Vision

* Python
* OpenCV
* MediaPipe
* NumPy

### ⚙️ Embedded Systems

* ESP32 / STM32
* Embedded C / ESP-IDF

### 🌐 Communication

* WiFi (HTTP / WebSocket based control)

---

## 🏗️ System Architecture

```
Hand Gesture (Camera)
        ↓
MediaPipe + OpenCV (Processing)
        ↓
Gesture Classification
        ↓
Send Command via WiFi
        ↓
ESP32 / STM32
        ↓
Motor Driver (L298N / ESC)
        ↓
Motor Movement
```

---

## 📸 How It Works

1. Camera captures hand gestures
2. MediaPipe detects hand landmarks
3. Gestures are classified (e.g., fist, open hand)
4. Commands are sent to microcontroller
5. Motors respond accordingly

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/builtbyMani/HandGesture-Recognition.git
cd HandGesture-Recognition
```

### 2. Install dependencies

```bash
pip install opencv-python mediapipe numpy
```

### 3. Run the program

```bash
python main.py
```

---

## ⚡ Hardware Setup

* ESP32 / STM32
* Motor Driver (L298N / ESC)
* DC Motors / BLDC Motors
* Power Supply (LiPo battery recommended)

---

## 🎮 Gesture Controls (Example)

| Gesture        | Action      |
| -------------- | ----------- |
| ✊ Fist         | Stop Motor  |
| ✋ Open Hand    | Start Motor |
| 👉 Point Right | Turn Right  |
| 👈 Point Left  | Turn Left   |

---

## 🔒 License

This project is licensed under the **Apache 2.0 License**.
You are free to use, modify, and distribute this project with proper attribution.

---

## 👨‍💻 Author

**Manikanta Srigade**

* Electronics Engineer (JNTU Hyderabad)
* Interested in Embedded Systems, AI, and Robotics

---

## ⭐ Future Improvements

* Add gesture-based speed control
* Integrate Kalman filter for smoother tracking
* Improve latency with WebSockets
* Add mobile app interface

---

## 💡 Inspiration

This project bridges **AI + Embedded Systems**, enabling intuitive human-machine interaction using just hand gestures.

---

⭐ If you found this useful, consider starring the repo!
