🚦 Project Name- **Traffic Management System**<br>

--------------------------------------

📖 **Overview**

The Traffic Management System is a computer-vision-based web application that helps manage traffic flow intelligently by analyzing live traffic camera feeds. It captures real-time images from a webcam, detects vehicles using an object detection model (YOLO), and dynamically adjusts signal timings based on vehicle density.

------------------------------------

🧩 **Features**

🎥 Real-time Image Capture using the system webcam.

🤖 Vehicle Detection using the YOLO (You Only Look Once) object detection model.

🚗 Dynamic Traffic Signal Adjustment based on detected vehicle count.

🌐 Flask Web Interface for easy interaction and data visualization.

⚙️ Modular Design with separate files for capturing images and running detection.

-------------------------------------
📂 **Project Structure**<br>

--------------------------------------------
<br>
Traffic-Management-System/ <br>
│<br>
├── app.py                # Flask application to handle routes and backend logic<br>
├── capture.py            # Handles webcam image capture<br>
├── car_detection.py      # YOLO-based object detection module (custom)<br>
├── templates/<br>
│   └── index.html        # Frontend HTML interface<br>
├── static/<br>
│   └── ...               # CSS, JS, and image assets<br>
├── images/<br>
│   └── *.jpg             # Captured images<br>
└── README.md             # Project documentation<br>
------------------------------------------------------------------
<br>
🧠 **How It Works**

1 Capture Phase (capture.py)

2 Opens the webcam and captures images in regular intervals.

3 Saves them in the /images folder.

4 Detection Phase (car_detection.py)

5 YOLO detects and counts vehicles in each image.

6 Returns the count of detected objects.

7 Decision Phase (app.py)

8 Flask receives detection results.

9 Computes total vehicle count per signal.

10 Returns optimized traffic signal timings.

--------------------------------------------------------------
 **Requirements**

- Python 3.8+
- Flask
- OpenCV (cv2)
- YOLO model and dependencies (PyTorch or TensorFlow)

Webcam

📊 Output Example

API Response (JSON):

{
  "signal_times": [25, 40, 15, 30]
}


(Each value represents the green signal duration for a lane based on vehicle count.)

![WhatsApp Image 2025-10-14 at 8 15 37 PM (1)](https://github.com/user-attachments/assets/446dd4d9-5bd6-4007-869c-67e6fac7dbbc)
https://github.com/akshadamahadik/Eco-Traffic-A-Sustainable-Approach-to-Urban-Mobility/releases/tag/v1.0

