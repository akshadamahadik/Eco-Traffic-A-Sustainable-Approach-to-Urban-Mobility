🚦 Traffic Management System
📖 Overview

The Traffic Management System is a computer-vision-based web application that helps manage traffic flow intelligently by analyzing live traffic camera feeds. It captures real-time images from a webcam, detects vehicles using an object detection model (YOLO), and dynamically adjusts signal timings based on vehicle density.

🧩 Features

🎥 Real-time Image Capture using the system webcam.

🤖 Vehicle Detection using the YOLO (You Only Look Once) object detection model.

🚗 Dynamic Traffic Signal Adjustment based on detected vehicle count.

🌐 Flask Web Interface for easy interaction and data visualization.

⚙️ Modular Design with separate files for capturing images and running detection.

📂 Project Structure
Traffic-Management-System/
│
├── app.py                # Flask application to handle routes and backend logic
├── capture.py            # Handles webcam image capture
├── car_detection.py      # YOLO-based object detection module (custom)
├── templates/
│   └── index.html        # Frontend HTML interface
├── static/
│   └── ...               # CSS, JS, and image assets
├── images/
│   └── *.jpg             # Captured images
└── README.md             # Project documentation
🧠 How It Works

Capture Phase (capture.py)

Opens the webcam and captures images in regular intervals.

Saves them in the /images folder.

Detection Phase (car_detection.py)

YOLO detects and counts vehicles in each image.

Returns the count of detected objects.

Decision Phase (app.py)

Flask receives detection results.

Computes total vehicle count per signal.

Returns optimized traffic signal timings.

🛠️ Requirements

Python 3.8+

Flask

OpenCV (cv2)

YOLO model and dependencies (PyTorch or TensorFlow)

Webcam

📊 Output Example

API Response (JSON):

{
  "signal_times": [25, 40, 15, 30]
}


(Each value represents the green signal duration for a lane based on vehicle count.)

![WhatsApp Image 2025-10-14 at 8 15 37 PM (1)](https://github.com/user-attachments/assets/446dd4d9-5bd6-4007-869c-67e6fac7dbbc)

