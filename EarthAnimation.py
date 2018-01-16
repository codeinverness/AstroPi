#Create an animation of the Earth
from sense_hat import SenseHat
import time

sense = SenseHat()

G = (0, 255, 0)
B = (0, 0, 255)
W = (255,255,255)
O = (0,0,0)

#For the animation we need several images to make it look like the Earth is rotating
earthAnimation_1 = [
    O, O, O, O, O, O, O, O,
    O, B, W, W, W, G, O, O,
    G, B, B, W, W, B, B, O,
    B, G, B, G, B, G, G, O,
    G, G, B, B, G, B, G, O,
    B, B, G, B, B, B, B, O,
    O, W, W, W, B, B, O, O,
    O, O, O, O, O, O, O, O,
    ]
    
earthAnimation_2 = [
    O, O, O, O, O, O, O, O,
    O, G, B, W, W, W, O, O,
    B, G, B, B, W, W, B, O,
    B, B, G, B, G, B, G, O,
    B, G, G, B, B, G, B, O,
    G, B, B, G, B, B, B, O,
    O, B, W, W, W, B, O, O,
    O, O, O, O, O, O, O, O,
    ]

earthAnimation_3 = [
    O, O, O, O, O, O, O, O,
    O, G, G, B, W, W, O, O,
    B, B, G, B, B, W, W, O,
    B, B, B, G, B, G, B, O,
    B, B, G, G, B, B, G, O,
    B, G, B, B, G, B, B, O,
    O, B, B, W, W, W, O, O,
    O, O, O, O, O, O, O, O,
    ]

earthAnimation_4 = [
    O, O, O, O, O, O, O, O,
    O, W, G, G, B, W, O, O,
    G, B, B, G, B, B, W, O,
    G, B, B, B, G, B, G, O,
    B, B, B, G, G, B, B, O,
    B, B, G, B, B, G, B, O,
    O, W, B, B, W, W, O, O,
    O, O, O, O, O, O, O, O,
    ]

earthAnimation_5 = [
    O, O, O, O, O, O, O, O,
    O, G, W, G, G, B, O, O,
    B, G, B, B, G, B, B, O,
    G, G, B, B, B, G, B, O,
    G, B, B, B, G, G, B, O,
    B, B, B, G, B, B, G, O,
    O, B, W, B, B, W, O, O,
    O, O, O, O, O, O, O, O,
    ]

earthAnimation_6 = [
    O, O, O, O, O, O, O, O,
    O, W, G, W, G, G, O, O,
    B, B, G, B, B, G, B, O,
    G, G, G, B, B, B, G, O,
    G, G, B, B, B, G, G, O,
    B, B, B, B, G, B, B, O,
    O, B, B, B, B, B, O, O,
    O, O, O, O, O, O, O, O,
    ]

earthAnimation_7 = [
    O, O, O, O, O, O, O, O,
    O, G, G, G, W, G, O, O,
    W, B, B, G, B, B, G, O,
    B, G, G, B, B, B, B, O,
    G, B, G, B, B, B, G, O,
    B, B, B, B, B, G, B, O,
    O, W, B, B, B, B, O, O,
    O, O, O, O, O, O, O, O,
    ]

earthAnimation_8 = [
    O, O, O, O, O, O, O, O,
    O, W, G, G, G, W, O, O,
    W, W, B, B, G, B, B, O,
    G, B, G, G, B, B, B, O,
    B, G, B, G, B, B, B, O,
    B, B, B, B, B, B, G, O,
    O, W, W, B, B, B, O, O,
    O, O, O, O, O, O, O, O,
    ]

earthAnimation_8 = [
    O, O, O, O, O, O, O, O,
    O, W, W, G, G, G, O, O,
    B, W, W, B, B, G, B, O,
    B, G, B, G, G, B, B, O,
    G, G, B, B, B, G, B, O,
    B, B, B, B, B, B, B, O,
    O, W, W, W, B, B, O, O,
    O, O, O, O, O, O, O, O,
    ]

earthAnimation_8 = [
    O, O, O, O, O, O, O, O,
    O, W, W, W, G, G, O, O,
    B, B, W, W, B, B, G, O,
    B, B, G, B, G, G, B, O,
    G, G, G, B, B, B, G, O,
    B, B, B, B, B, B, B, O,
    O, W, W, W, W, B, O, O,
    O, O, O, O, O, O, O, O,
    ]

earthAnimation_end = [
    O, O, O, O, O, O, O, O,
    O, B, W, W, W, G, O, O,
    G, B, B, W, W, B, B, O,
    B, G, B, G, B, G, G, O,
    G, G, B, B, G, B, G, O,
    B, B, G, B, B, B, B, O,
    O, W, W, W, B, B, O, O,
    O, O, O, O, O, O, O, O,
    ]

#Create the animation
while True: 
    sense.set_pixels(earthAnimation_1)
    time.sleep(1)
    sense.set_pixels(earthAnimation_2)
    time.sleep(1)
    sense.set_pixels(earthAnimation_3)
    time.sleep(1)
	sense.set_pixels(earthAnimation_4)
    time.sleep(1)
	sense.set_pixels(earthAnimation_5)
    time.sleep(1)
	sense.set_pixels(earthAnimation_6)
    time.sleep(1)
	sense.set_pixels(earthAnimation_7)
    time.sleep(1)
	sense.set_pixels(earthAnimation_8)
    time.sleep(1)
	sense.set_pixels(earthAnimation_9)
    time.sleep(1)