from flask import Flask, request, jsonify, render_template
from datetime import datetime
import random

app = Flask(__name__)
sensor_data = {"temperature": None, "humidity": None}

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(sensor_data)

@app.route('/simulate')
def simulate_sensor():
    sensor_data['temperature'] = round(random.uniform(20, 30), 2)
    sensor_data['humidity'] = round(random.uniform(40, 70), 2)
    print(f"Simulated data at {datetime.now()}: {sensor_data}")
    return jsonify({"status": "simulated", "data": sensor_data})

@app.route('/sensor', methods=['POST'])
def sensor():
    data = request.get_json()
    sensor_data['temperature'] = data.get('temperature')
    sensor_data['humidity'] = data.get('humidity')
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
