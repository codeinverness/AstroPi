from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

G = (0, 255, 0)
B = (0, 0, 255)
W = (255,255,255)
O = (0,0,0)

def earth_animation1():
    image = [
    O, O, W, W, W, B, O, O,
    O, G, B, B, B, G, G, O,
    G, G, B, B, G, B, G, G,
    G, G, B, B, G, G, G, G,
    G, B, B, G, G, B, G, B,
    G, G, B, G, G, B, B, G,
    O, G, B, W, B, B, B, O,
    O, O, W, W, W, W, O, O,
    ]
    return image

def earth_animation2():
    image = [
    O, O, W, W, W, W, O, O,
    O, G, G, G, B, B, B, O,
    G, G, G, G, B, B, G, B,
    B, G, G, G, B, B, G, G,
    B, B, G, B, B, G, G, B,
    B, B, G, G, B, G, G, B,
    O, B, B, G, B, W, B, O,
    O, O, W, W, W, W, O, O,
    ]
    return image
    
def earth_animation3():
    image = [
    O, O, W, B, W, W, O, O,
    O, B, B, G, G, G, B, O,
    B, B, G, G, G, G, B, B,
    B, B, B, G, G, G, B, B,
    B, B, B, B, G, B, B, G,
    B, G, B, B, G, G, B, G,
    O, B, B, B, B, G, B, O,
    O, O, W, W, W, W, O, O,
    ]
    return image
    
def earth_animation4():
    image = [
    O, O, W, W, W, B, O, O,
    O, G, B, B, B, G, G, O,
    B, B, B, B, G, G, G, G,
    B, G, B, B, B, G, G, G,
    B, B, B, B, B, B, G, B,
    G, G, B, G, B, B, G, G,
    O, G, B, B, B, B, B, O,
    O, O, W, W, W, W, O, O,
    ]
    return image
    
def earth_animation5():
    image = [
    O, O, W, B, W, W, O, O,
    O, G, G, B, B, B, B, O,
    G, G, B, G, B, B, G, G,
    G, G, B, G, B, B, B, G,
    B, B, B, B, B, B, B, B,
    G, G, B, G, B, B, G, G,
    O, G, B, B, B, B, B, O,
    O, O, W, W, W, W, O, O,
    ]
    return image
    
def earth_animation6():
    image = [
    O, O, W, W, W, W, O, O,
    O, B, G, G, G, B, B, O,
    G, G, G, G, B, G, B, B,
    B, G, G, G, B, G, B, B,
    G, B, B, B, B, B, B, B,
    B, B, G, G, B, G, B, B,
    O, W, B, G, B, B, B, O,
    O, O, W, W, W, W, O, O,
    ]
    return image
    
def earth_animation7():
    image = [
    O, O, W, W, W, W, O, O,
    O, G, G, B, G, B, G, O,
    G, B, G, G, B, G, B, G,
    G, G, G, G, B, B, B, G,
    G, B, G, B, B, B, G, B,
    G, B, B, G, B, B, B, B,
    O, B, B, B, G, B, B, O,
    O, O, W, W, W, W, O, O,
    ]
    return image

def earth_animation8():
    image = [
    O, O, W, W, W, W, O, O,
    O, B, B, G, G, B, G, O,
    B, B, G, B, G, G, B, G,
    B, B, G, G, G, G, B, B,
    B, G, G, B, G, B, B, B,
    B, G, G, B, B, G, B, B,
    O, W, B, B, B, B, G, O,
    O, O, W, W, W, W, O, O,
    ]
    return image
    
images = [earth_animation1, earth_animation2, earth_animation3, earth_animation4, earth_animation5, earth_animation6, earth_animation7, earth_animation8]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
