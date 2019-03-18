from flask import Flask, jsonify, render_template, send_file
from sense_hat import SenseHat
from picamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/json')
def json():
    sense = SenseHat()

    return jsonify(name='Vegard Alvsaker', telephone='454 82 059', temp=sense.get_temperature())

@app.route('/get_image')
def get_image():
    camera = picamera.PiCamera()

    camera.capture()
    camera.close()
    return send_file('ronny.jpg', mimetype='image/gif')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
