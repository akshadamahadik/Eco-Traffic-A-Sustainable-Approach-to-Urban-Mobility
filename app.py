from flask import Flask, render_template, jsonify
from car_detection import YOLOObjectDetection as car  # Your custom module for detection
import capture
import time
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render your HTML page

@app.route('/get_signal_times')
def get_signal_times():
    for i in range(3):
        capture.capture(str(1)+".jpg")
        time.sleep(30)
    results = car.main()  # Run car detection logic
    signals = [sum(obj_counts.values()) for obj_counts in results.values()]
    return jsonify({"signal_times": signals})  # Send data to frontend

if __name__ == '__main__':
    app.run(debug=True)
