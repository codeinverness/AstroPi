#Version 3
#Print out to Sense Hat

#Import SenseHat
from sense_hat import SenseHat
sense = SenseHat()
import ephem
import time

#ISS Two Line telemetry
name = "ISS"
line1 = "1 25544U 98067A   17320.58149788  .00003295  00000-0  56951-4 0  9992"
line2 = "2 25544  51.6424 358.6134 0004424 120.6220  11.4433 15.54157095 85451"

#Calculate the ISS location using ephem and pass that back to ISS variable
ISS = ephem.readtle(name, line1, line2)
ISS.compute()

#Convert to Strings
ISSlongString = str(ISS.sublong)
ISSlatString = str(ISS.sublat)

ISSlong = ISSlongString.split(":")
ISSlat = ISSlatString.split(":")

#Convert to floating point numbers for checking ranges
ISSlong[0] = float(ISSlong[0])
ISSlat[0] = float(ISSlat[0])

print ISSlong[0]
print ISSlat[0]

#Main loop to run and keep checking position
while True:
	#Is the ISS between these positions?
	if(ISSlong[0] >= -100 and ISSlong[0] <= -7) and (ISSlat[0] >= -400 and ISSlat[0] <= -1):
		
		#If so print "YAY!" and location
		sense.show_message("Yay! I found the ISS!")
		print ISS.sublong, ISS.sublat
		
		#Sleep and recalculate
		time.sleep(5)
		ISS.compute()
	
	#If not then do this set of commands print "Where?", location, sleep and recalculate
	else:
		print ("Where on Earth is the ISS?")
		print ISS.sublong, ISS.sublat
		time.sleep(5)
		ISS.compute()
