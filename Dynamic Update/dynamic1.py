
from data import tempp, humii, sensor
from flask import Flask, jsonify, render_template, request, send_from_directory
import webbrowser
import time
# from camera import VideoCamera


# pi_camera = VideoCamera(flip=False)
app = Flask(__name__)
temp = 1
humi = 1
mq9 = 1
allert = 1


@app.route('/_stuff', methods=['GET'])
def stuff():
    return jsonify(temp=tempp(tempp), humi=humii(humi), mq9=sensor(mq9), mq8=1)


@app.route('/')
def index():
    return render_template('dy1.html')


@app.route('/intro')
def intr():
    return render_template('intro.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(pi_camera),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


# def gen(camera):
#     get camera frame
#     while True:
#        frame = camera.get_frame()
#        yield (b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
if __name__ == '__main__':

    app.run(host='0.0.0.0', port='2023', debug=True)
