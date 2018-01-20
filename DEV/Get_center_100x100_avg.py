#This code takes an image and returns a value for the average of the center 100x100 pixels
#
#Revision 1 - 2018-01-20 - Inital Commit

from picamera import PiCamera
from time import sleep
from PIL import Image
dir = '/home/pi/tmp/test.jpg'


camera = PiCamera()
camera.resolution = (2592, 1944) #set the resolution of the camera to as big as possible
camera.framerate = 15 #set the cameras framerate
camera.start_preview() #start the viewer
sleep(5) #wait for the image to stabalise
camera.capture(dir) #take an image and save to working directory
camera.stop_preview()

openimage = Image.open(dir) #open the image in pillow
cropbox = (1246,922,1346,1022)
croppedimage = openimage.crop(cropbox) #take only the center 100x100 pixels
dir = '/home/pi/tmp/test2.jpg' #DEBUG set file path to a new name
croppedimage.save(dir) #DEBUG save the image to a file
openimage = Image.open(dir) #DEBUG reopen the image
print(openimage.getcolors(25555)) #Return a list of colours
exit()