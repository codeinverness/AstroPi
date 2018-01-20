#This code takes an image and returns a value for the average of the center 100x100 pixels
#
#Revision 1 - 2018-01-20 - Inital Commit

from picamera import PiCamera
from time import sleep
from PIL import Image

camera = PiCamera

camera.resolution(2592, 1944)
camera.start_preview()
sleep(5)
dir = '~/tmp/test.bmp'
camera.capture(dir)

Image.open(dir)
Image.crop(1246,922,1346,1022)
dir = '~/tmp/test2.bmp'
Image.save(dir)
Image.open(dir)
print(Image.getcolours(25555))
exit()