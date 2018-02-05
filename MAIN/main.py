#This code takes images from the ISS and determines if the ISS is over land or sea
#
# Revision 1 - 2018-01-21 - Inital Commit based on Dev work done 2018-01-20
#
# most_frequent_color and average_colour used by permission from:
# https://github.com/ZeevG/python-dominant-image-colour

# Start Camera    **DONE**
# Setup CSV and write headers    **DONE**
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
import ephem

imagefile = 10000
imagename = ''
imagename2 = ''
timestamp = datetime.datetime.now()
datafile = ''
whatispicture = ''
logfile = "log.csv"
animation = []

GPS_lat = ''
GPS_long = ''

G = (0, 255, 0)
B = (0, 0, 255)
W = (255,255,255)
O = (0,0,0)
R = (255, 0, 0)


landref = "land.txt"
landtupples = []
searef = "sea.txt"
seatupples = []
cloudref = "cloud.txt"
cloudtupples = []
nightref = "night.txt"
nighttupples = []

name = "ISS"
line1 = "1 25544U 98067A   17320.58149788  .00003295  00000-0  56951-4 0  9992"
line2 = "2 25544  51.6424 358.6134 0004424 120.6220  11.4433 15.54157095 85451"

earth_animation1 = [
O, O, W, W, W, B, O, O,
O, G, B, B, B, G, G, O,
G, G, B, B, G, B, G, G,
G, G, B, B, G, G, G, G,
G, B, B, G, G, B, G, B,
G, G, B, G, G, B, B, G,
O, G, B, W, B, B, B, O,
O, O, W, W, W, W, O, O,
]

earth_animation2 = [
O, O, W, W, W, W, O, O,
O, G, G, G, B, B, B, O,
G, G, G, G, B, B, G, B,
B, G, G, G, B, B, G, G,
B, B, G, B, B, G, G, B,
B, B, G, G, B, G, G, B,
O, B, B, G, B, W, B, O,
O, O, W, W, W, W, O, O,
]
    
earth_animation3 = [
O, O, W, B, W, W, O, O,
O, B, B, G, G, G, B, O,
B, B, G, G, G, G, B, B,
B, B, B, G, G, G, B, B,
B, B, B, B, G, B, B, G,
B, G, B, B, G, G, B, G,
O, B, B, B, B, G, B, O,
O, O, W, W, W, W, O, O,
]
    
earth_animation4 = [
O, O, W, W, W, B, O, O,
O, G, B, B, B, G, G, O,
B, B, B, B, G, G, G, G,
B, G, B, B, B, G, G, G,
B, B, B, B, B, B, G, B,
G, G, B, G, B, B, G, G,
O, G, B, B, B, B, B, O,
O, O, W, W, W, W, O, O,
]
    
earth_animation5 = [
O, O, W, B, W, W, O, O,
O, G, G, B, B, B, B, O,
G, G, B, G, B, B, G, G,
G, G, B, G, B, B, B, G,
B, B, B, B, B, B, B, B,
G, G, B, G, B, B, G, G,
O, G, B, B, B, B, B, O,
O, O, W, W, W, W, O, O,
]

    
earth_animation6 = [
O, O, W, W, W, W, O, O,
O, B, G, G, G, B, B, O,
G, G, G, G, B, G, B, B,
B, G, G, G, B, G, B, B,
G, B, B, B, B, B, B, B,
B, B, G, G, B, G, B, B,
O, W, B, G, B, B, B, O,
O, O, W, W, W, W, O, O,
]

earth_animation7 = [
O, O, W, W, W, W, O, O,
O, G, G, B, G, B, G, O,
G, B, G, G, B, G, B, G,
G, G, G, G, B, B, B, G,
G, B, G, B, B, B, G, B,
G, B, B, G, B, B, B, B,
O, B, B, B, G, B, B, O,
O, O, W, W, W, W, O, O,
]

earth_animation8 = [
O, O, W, W, W, W, O, O,
O, B, B, G, G, B, G, O,
B, B, G, B, G, G, B, G,
B, B, G, G, G, G, B, B,
B, G, G, B, G, B, B, B,
B, G, G, B, B, G, B, B,
O, W, B, B, B, B, G, O,
O, O, W, W, W, W, O, O,
]

animation = [earth_animation1, earth_animation2, earth_animation3, earth_animation4, earth_animation5, earth_animation6, earth_animation7, earth_animation8]



def most_frequent_color(image):
    w, h = image.size
    pixels = image.getcolors(w * h)
    most_frequent_pixel = pixels[0]
    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)
    return most_frequent_pixel

#def average_color(image):
#    color_tuple = [None, None, None]
#    for channel in range(3): #Get data for one channel at a time
#        pixels = image.getdata(band=channel)
#        values = []
#        for pixel in pixels:
#            values.append(pixel)
#        color_tuple[channel] = int(round((sum(values) / len(values)),0), base=10)
#    return tuple(color_tuple)

def startcamera():
    camera = PiCamera()
    camera.resolution = (2592, 1944) #set the resolution of the camera to as big as possible
    camera.framerate = 15 #set the cameras framerate
    camera.start_preview() #start the viewer
    sleep(5) #wait for the image to stabalise

def takepicture():
	getgps()
	info = []
	info.append(team_name)
	info.append(dt.datetime.now().strftime(time_format))
	info.append("Lat: " + GPS_lat)
	info.append("Long: " + GPS_long)
	cam.annotate_text = "\n".join(info)
	
	camera.capture(imagename) #take an image and save to working directory
	openimage = Image.open(imagename) #open the image in pillow
	cropbox = (1246,922,1346,1022) #define the center 100x100 pixels
	croppedimage = openimage.crop(cropbox) #take only the center 100x100 pixels
	croppedimage.save(imagename2) #save the center 100x100 as a new file
	
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
	sense_data = str(imagefile)+", "+sense_data+", "+GPS_long+", "+GPS_long+", "+whatispicture
	print(sense_data)
	fh = open("logfile", "w") 
	fh.write(sense_data)
	fh.close() 
	
def earthsea():
	openimage = Image.open(imagename2) #open the cropped file
	tmptupple = most_frequent_color(openimage)
	if tmptupple in landtupples:
		whatispicture = 'Land'
	elif tmptupple in seatupples:
		whatispicture = 'Sea'
	elif tmptupple in cloudtupples:
		whatispicture = 'Cloud'
	elif tmptupple in nighttupples:
		whatispicture = 'Night'
	else:
		whatispicture = 'UNKNOWN'

def idleanimation():
	for count in range(6):
		sense.set_pixels(animation[count])
		sleep(5)

def readdata():
	landtupples = open(landref,'r').read().split('\n')
	seatupples = open(searef,'r').read().split('\n')
	cloudtupples = open(cloudref,'r').read().split('\n')
	nighttupples = open(nightref,'r').read().split('\n')

def writeheader():
	Header = "Temp, Humidity, Pressure, yaw, pitch, roll, mag_x, mag_y, mag_z, acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z, gps_x, gps_y, whatispicture"
	fh = open("logfile", "w") 
	fh.write(Header)
	fh.close() 

def getgps():
	ISS = ephem.readtle(name, line1, line2)
	ISS.compute()
	GPS_lat = ISS.sublat
	GPS_long = ISS.sublong
	
startcamera()
writeheader()
readdata()
sense.show_message("Ready!", text_colour = G)
while True:
	sense.set_pixels(animation[7])
	nextimagename()
	takepicture()
	earthsea()
	getlogdata()
	savelogdata()
	idleanimation()
	
	
#print(most_frequent_color(openimage))
#print(average_color(openimage))
#print()

exit()
