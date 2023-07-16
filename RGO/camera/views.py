from django.views.decorators import gzip
from django.http import StreamingHttpResponse

import threading
import cv2
import rtsp
import numpy as np
from time import sleep
from multiprocessing import Process

#### Start view of camera ############################
#### Display Camera in index.html ###################
f = 0


##### Camera 1
@gzip.gzip_page
def webcam_feed_0(request):
    try:
        cam = VideoCamera('ip')
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print(e)
        pass

##### Camera 2
@gzip.gzip_page
def webcam_feed_1(request):
    try:
        cam = VideoCamera('ip')
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print(e)
        pass
    
##### Camera 3
@gzip.gzip_page
def webcam_feed_2(request):
    try:
        cam = VideoCamera('ip')
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print(e)
        pass

##### Camera 4
@gzip.gzip_page
def webcam_feed_3(request):
    try:
        cam = VideoCamera('ip')
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print(e)
        pass

##### Camera 5
@gzip.gzip_page
def webcam_feed_4(request):
    try:
        cam = VideoCamera('ip')
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print(e)
        pass

##### Camera 6
@gzip.gzip_page
def webcam_feed_5(request):
    try:
        cam = VideoCamera('ip')
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print(e)
        pass

#to capture video class
class VideoCamera(object):
    def __init__(self, url):
        self.url = url
        self.video = rtsp.Client(url)
        sleep(1)
        self.frame = self.video.read(raw=True)
        # self.update()
        threading.Thread(target=self.update, daemon=True, args=()).start()

    def get_frame(self):
        image = self.frame
        print(image.shape)
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        global f
        while True:
            self.frame = self.video.read(raw=True)
            cv2.waitKey(1)


def gen(camera):
   while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

