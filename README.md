# Flask-opencv webcam streaming server #
This is a simple python3 script that serves a tiny Flask video webserver that allows to take photos or see real time video streaming of a connected camera/webcam controlled with opencv.

## Requirements ##
In order to execute the script you need to install opencv3 -> `import cv2` and some python modules.

Move to the project folder and try:

### Try #1: ###
```
pip install -r requirements.txt
```

### Try #2: ###
```
pip install flask opencv-python
```
If it gets any error, probably with `opencv-python` try to install them manually.

## Running ##
To start the service `cd` to project folder and type `python server.py` or `python3 server.py`

*It only runs on python3*

Once done navigate to the ip of the server and access the port `5000`.

http://localhost:5000

## Configuration ##
### Change running port ###
The project is default configured to run at port 5000. To change the running port you must specify the argument `-p, --port [PORT]`.

*Example:*

```python3 server.py -p 3000 ``` Runs on port 3000

### Change camera source ###
To change the camera source of opencv you can go to the beginning of file `server.py` and add a `video_source=1` it can be 0,1,2... as many video inputs the device has in the declaration of object `Camera`. Or you can change the default video source on `camera.py` `Camera` class `__init__` method.

