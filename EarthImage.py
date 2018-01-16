# Create an animation of the Earth
# We need to use the time and Sense Hat functions

from sense_hat import SenseHat
import time

sense = SenseHat()

G = (0, 255, 0)
B = (0, 0, 255)
W = (255, 255, 255)
O = (0, 0, 0)

# For the animation we need several images to make it look like the Earth is rotating
earthImage_1 = [
    O, O, O, O, O, O, O, O,
    O, B, W, W, W, G, O, O,
    G, B, B, W, W, B, G, O,
    B, G, B, G, B, G, G, O,
    G, G, B, B, G, B, G, O,
    B, B, G, B, B, B, G, O,
    O, W, W, W, B, G, O, O,
    O, O, O, O, O, O, O, O,
]

# Create the animation
while True:
    sense.set_pixels(earthImage_1)
