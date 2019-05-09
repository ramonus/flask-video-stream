from flask import Flask, render_template, request, send_from_directory, Response
from flask_socketio import SocketIO
from pathlib import Path
from capture import capture_and_save
from camera import Camera


app = Flask(__name__)
# app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering or Chrome Frame,
    and also to cache the rendered page for 10 minutes
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers["Cache-Control"] = "public, max-age=0"
    return r

@app.route("/")
def entrypoint():
    return render_template("index.html")

@app.route("/r")
def capture():
    capture_and_save()
    return render_template("send_to_init.html")

@app.route("/images/last")
def last_image():
    p = Path("images/last.png")
    if p.exists():
        r = "last.png"
    else:
        print("No last")
        r = "not_found.jpeg"
    return send_from_directory("images",r)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')

@app.route("/stream")
def stream_page():
    return render_template("stream.html")

@app.route("/video_feed")
def video_feed():
    return Response(gen(Camera()),
        mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__=="__main__":
    socketio.run(app,host="0.0.0.0",port="3005")