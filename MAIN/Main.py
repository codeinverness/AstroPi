#This code takes images from the ISS and determines if the ISS is over land or sea
#
# Revision 1 - 2018-01-21 - Inital Commit based on Dev work done 2018-01-20
#
# most_frequent_color and average_colour used by permission from:
# https://github.com/ZeevG/python-dominant-image-colour

# Start Camera
# Setup CSV and write headers
# Display "Ready"
# Open Loop
#   Show Picture
#   Setup Image File Names using imagefile (imgdir1, imgdir2)
#   Read Sensors
#   Take Image
#   Save image as imgdir1
#   open immage and proceess, saving the cropped image as imgdir2
#   Build String and append to file
#   carry out annimation




import datetime
from picamera import PiCamera
from time import sleep
from PIL import Image
from sense_hat import SenseHat

dir = '/home/pi/tmp/test.jpg'
imagefile = 10001
timestamp = datetime.datetime.now()
datafile = ''


def most_frequent_color(image):
    w, h = image.size
    pixels = image.getcolors(w * h)
    most_frequent_pixel = pixels[0]
    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)
    return most_frequent_pixel

def average_color(image):
    color_tuple = [None, None, None]
    for channel in range(3): #Get data for one channel at a time
        pixels = image.getdata(band=channel)
        values = []
        for pixel in pixels:
            values.append(pixel)
        color_tuple[channel] = int(round((sum(values) / len(values)),0), base=10)
    return tuple(color_tuple)

def startcamera():
    camera = PiCamera()
    camera.resolution = (2592, 1944) #set the resolution of the camera to as big as possible
    camera.framerate = 15 #set the cameras framerate
    camera.start_preview() #start the viewer
    sleep(5) #wait for the image to stabalise

startcamera()

camera.capture(dir) #take an image and save to working directory
openimage = Image.open(dir) #open the image in pillow
cropbox = (1246,922,1346,1022)
croppedimage = openimage.crop(cropbox) #take only the center 100x100 pixels
croppedimage.save(dir) #DEBUG save the image to a file
openimage = Image.open(dir) #DEBUG reopen the image

#print(most_frequent_color(openimage))
#print(average_color(openimage))
#print()

exit()