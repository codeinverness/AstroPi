#This code takes images from the ISS and determines if the ISS is over land or sea
#
# Revision 1 - 2018-01-21 - Inital Commit based on Dev work done 2018-01-20
#
# most_frequent_color and average_colour used by permission from:
# https://github.com/ZeevG/python-dominant-image-colour

# Start Camera    **DONE**
# Setup CSV and write headers
# Display "Ready"    **DONE**
# Open Loop
#   Show Picture
#   Setup Image File Names using imagefile (imgdir1, imgdir2)    **DONE**
#   Read Sensors    **DONE**
#   Take Image    **DONE**
#   Save image as imgdir1    **DONE**
#   open immage and proceess, saving the cropped image as imgdir2    **DONE**
#   Build String and append to file    **DONE**
#   carry out annimation




import datetime
from picamera import PiCamera
from time import sleep
from PIL import Image
from sense_hat import SenseHat

imagefile = 10000
imagename = ''
imagename2 = ''
timestamp = datetime.datetime.now()
datafile = ''
whatispicture = ''
logfile = "log.csv"
green = (0, 255, 0)

landref = "land.txt"
landtupples = []
searef = "sea.txt"
seatupples = []
cloudref "cloud.txt"
cloudtupples = []


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

def takepicture():
	camera.capture(imagename) #take an image and save to working directory
	openimage = Image.open(imagename) #open the image in pillow
	cropbox = (1246,922,1346,1022) #define the center 100x100 pixels
	croppedimage = openimage.crop(cropbox) #take only the center 100x100 pixels
	croppedimage.save(imagename2) #save the center 100x100 as a new file
	openimage = Image.open(imagename2) #reopen the same file

def nextimagename():
	imagefile = imagefile+1
	imagename = str(imagefile)+"_HR.jpg"
	imagename2  = str(imagefile)+"_100x100.jpg"

def getlogdata():
	sense_data=[]
	sense_data.append(sense.get_temperature())
	sense_data.append(sense.get_humidity())
	sense_data.append(sense.get_pressure())

	o = sense.get_orientation()
	yaw = o["yaw"]
	pitch = o["pitch"]
	roll = o["roll"]
	sense_data.extend([pitch,roll,yaw])

	mag = sense.get_compass_raw()
	mag_x = mag["x"]
	mag_y = mag["y"]
	mag_z = mag["z"]
	sense_data.extend([mag_x,mag_y,mag_z])

	acc = sense.get_accelerometer_raw()
	x = acc["x"]
	y = acc["y"]
	z = acc["z"]
	sense_data.extend([x,y,z])

	gyro = sense.get_gyroscope_raw()
	gyro_x = gyro["x"]
	gyro_y = gyro["y"]
	gyro_z = gyro["z"]
	sense_data.extend([gyro_x,gyro_y,gyro_z])

	sense_data.append(datetime.datetime.now())
	return sense_data
	
def savelogdata():
	sense_data = str(getlogdata())
	sense_data = sense_data[1:-1]
	sense_data = str(imagefile)+", "+sense_data+", "+whatispicture
	print(sense_data)
	fh = open(logfile, “w”) 
	fh.write(sense_data)
	fh.close() 
	
def earthsea():
	
def idleanimation():


startcamera()
sense.show_message("Ready!", text_colour = green)

file = open(landref, “r”) 
for line in file: 
	landtupples.append(line) 
file = open(searef, “r”) 
for line in file: 
	seatupples.append(line) 	
file = open(cloudref, “r”) 
for line in file: 
	cloudtupples.append(line) 

#print(most_frequent_color(openimage))
#print(average_color(openimage))
#print()

exit()