#Using ephem and two line telemetry
import ephem
import time

#ISS Two line telemetry
name = "ISS"
line1 = "1 25544U 98067A   17320.58149788  .00003295  00000-0  56951-4 0  9992"
line2 = "2 25544  51.6424 358.6134 0004424 120.6220  11.4433 15.54157095 85451"

#Calculate the GPS using ephem and passing TLE data
ISS = ephem.readtle(name, line1, line2)
ISS.compute()

while True:
	print ISS.sublong, ISS.sublat
	time.sleep(5)
	ISS.compute()
