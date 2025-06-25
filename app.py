from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
sensor_data = {"temperature": None, "humidity": None}

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(sensor_data)

@app.route('/sensor', methods=['POST'])
def sensor():
    data = request.get_json()
    sensor_data['temperature'] = data.get('temperature')
    sensor_data['humidity'] = data.get('humidity')
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)
