# This code takes a directory of image files and returns a list of the averages of the center 100x100 pixels
#
# Revision 1 - 2018-01-30 - Inital Commit
# 
# average_color and most_frequent_color used by permission from
# https://github.com/ZeevG/python-dominant-image-colour


import glob
from time import sleep
from PIL import Image
dir = 'test.jpg'

def most_frequent_color(image):
    w, h = image.size
    pixels = image.getcolors(w * h)
    most_frequent_pixel = pixels[0]
    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (colour)
    return most_frequent_pixel

imagelist = glob.glob('*.jpg')

fh = open("land.txt", "w") 
fh.close

for x in imagelist:
    fh = open("land.txt", "a")
    openimage = Image.open(x) #open the image in pillow
    fh.write(str(most_frequent_color(openimage)) + '\n')
    fh.close() 


exit()