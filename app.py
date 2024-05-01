from flask import Flask, render_template, Response
from exersise.LateralRaises import LateralRaises
from exersise.ShoulderPress import shoulderPress
from exersise.Curl import  curlCounter
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lateral_raises')
def LateralRaisesRoute():
    return Response(LateralRaises(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/shoulder_press")
def shouldPressRoute():
    return Response(shoulderPress(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/curl_counter")
def curlCounterRoute():
    return Response(curlCounter(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
