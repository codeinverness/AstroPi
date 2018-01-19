# Import the modules we need

import picamera
import time
import datetime as dt
import ephem

# Add the tag variables we want to use
team_name = "Code Inverness"
time_format = "%d/%m/%Y %H:%M:%S"

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   17332.28575632  .00003326  00000-0  57234-4 0  9993"
line2 = "2 25544  51.6431 300.2614 0004099 158.9129 343.4648 15.54248554 87274"

iss = ephem.readtle(name, line1, line2)

cam = picamera.PiCamera()
cam.start_preview(alpha=192)  # alpha = 192

cam.annotate_background = picamera.Color('black')
cam.annotate_text_size = 50

for i in range(5):
    iss.compute()

    info = []
    info.append(team_name)
    info.append(dt.datetime.now().strftime(time_format))
    info.append("Lat: " + str(iss.sublat))
    info.append("Long: " + str(iss.sublong))
    cam.annotate_text = "\n".join(info)

    time.sleep(1)

cam.capture("foo.jpg")
cam.stop_preview()
