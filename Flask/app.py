from flask import Flask, jsonify, render_template, send_file
from sense_hat import SenseHat
from picamera.camera import PiCamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/json')
def json():
    sense = SenseHat()

    return jsonify(name='Vegard Alvsaker', telephone='454 82 059', temp=round(sense.get_temperature(),2), humidity=round(sense.get_humidity(),2), pressure=round(sense.get_pressure(),2))

@app.route('/get_image')
def get_image():
    camera = PiCamera()

    camera.capture("ronny.jpg")
    camera.close()
    return send_file('ronny.jpg', mimetype='image/gif')

@app.route('/get_image2')
def get_image2():
    return send_file('photo1.JPEG', mimetype='image/gif')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
