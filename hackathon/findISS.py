# Task: Create a function which finds the GPS coordinates of the ISS

# wget http://www.celestrak.com/NORAD/elements/stations.txt

import ephem
import time

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   17332.28575632  .00003326  00000-0  57234-4 0  9993"
line2 = "2 25544  51.6431 300.2614 0004099 158.9129 343.4648 15.54248554 87274"
