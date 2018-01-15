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
    G, B, B, W, W, B, G, O,
    B, G, B, G, B, G, G, O,
    G, G, B, B, G, B, G, O,
    B, B, G, B, B, B, G, O,
    O, W, W, W, B, G, O, O,
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