import ephem
import time

name = "ISS"
line1 = "1 25544U 98067A   17320.58149788  .00003295  00000-0  56951-4 0  9992"
line2 = "2 25544  51.6424 358.6134 0004424 120.6220  11.4433 15.54157095 85451"

tle_rec = ephem.readtle(name, line1, line2)
tle_rec.compute()

if  (tle_rec.sublat >=55 and < 57) and (tle_rec.sublong >= -6 and < -0.5):
	print ("it works")
	time.sleep(5)
	tle_rec.compute()
else:
	print("it doesn't work")
