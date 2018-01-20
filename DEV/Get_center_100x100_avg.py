#This code takes an image and returns a value for the average of the center 100x100 pixels
#
#Revision 1 - 2018-01-20 - Inital Commit
#
# https://zeevgilovitz.com/detecting-dominant-colours-in-python

from picamera import PiCamera
from time import sleep
from PIL import Image
dir = '/home/pi/tmp/test.jpg'

def most_frequent_color(image):
    w, h = image.size
    pixels = image.getcolors(w * h)
    most_frequent_pixel = pixels[0]
    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)
    compare("Most Common", image, most_frequent_pixel[1])
    return most_frequent_pixel

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

print(most_frequent_color(openimage))

exit()