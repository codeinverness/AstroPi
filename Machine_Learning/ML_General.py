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
for x in imagelist:
	openimage = Image.open(x) #open the image in pillow
	w, h = openimage.size
	cropbox = (((w/2)-50),((h/2)-50),((w/2)+50),((h/2)+50)) #determine position of crop based on image res
	croppedimage = openimage.crop(cropbox) #take only the center 100x100 pixels
	tmpdir = './new/'+str(x) #DEBUG set file path to a new name
	croppedimage.save(tmpdir) #DEBUG save the image to a file
	print(x)
	print(most_frequent_color(croppedimage))
	print(average_color(croppedimage))
	print()

exit()