from flask import Flask, jsonify, render_template, send_file
import datetime
from sense_hat import SenseHat
from picamera.camera import PiCamera
from utils.utils import get_week_history, days_dict

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    #Gets the correct order of day names for the history table
    days = days_dict[now.strftime("%A")]
    #History is the weather data
    history = get_week_history()
    return render_template('index.html', history=history, days=days)

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
