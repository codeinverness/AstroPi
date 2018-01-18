# Watch a 10 second stream from camera

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=200) # Set the transparency of the camera alpha, can be any value between 0 and 255
sleep(10)
camera.stop_preview()