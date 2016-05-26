import os
import PIL
from PIL import Image
from PIL import ImageChops
import math

def main(directory="/Users/mgiraud/Documents/images/"):
    img = list()
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(".jpeg"):
                img.append(Image.open(directory + name))
    notblack={}
    i=0
    while i<len(img):
        x=0
        y=0
        for pixel in ImageChops.difference(img[i-1], img[i]).getdata():
            if greyscale(pixel) >25:
                if (x,y) in notblack:
                    notblack[(x,y)] = notblack[(x,y)] + 1
                else: notblack[(x,y)] = 1
            if(x<352): x+=1
            else:
                x=0
                y+=1
        i+=1
    return notblack

def completion(dictionary):
    y=0
    while y<288:
        x=0
        while x<352:
            if (x,y) not in dictionary:
                dictionary[(x,y)] = 0
            x +=1
        y+=1
    return dictionary

def greyscale(pixel):
    return math.sqrt(math.pow(pixel[0], 2) + math.pow(pixel[1], 2) + math.pow(pixel[2], 2))

####
