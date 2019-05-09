import cv2

class Camera:
    def __init__(self):
        self.vid = cv2.VideoCapture(0)
        with open("images/not_found.jpeg","rb") as f:
            self.nf = f.read()
    def get_frame(self):
        v,im = self.vid.read()
        if v:
            img = cv2.imencode(".png",im)[1].tobytes()
            return img
        else:
            return self.nf
