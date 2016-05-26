import os
import PIL
from PIL import Image
from PIL import ImageChops
import math
import matplotlib
from matplotlib import pyplot


def main(directory="/Users/mgiraud/Documents/images/"):
    img = list()
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(".jpg"):
                img.append(Image.open(directory + name))
    return img

def notBlack(img):
    notblack={}
    i=0
    while i<len(img):
        x=0
        y=0
        for pixel in ImageChops.difference(img[i-1], img[i]).getdata():
            if greyscale(pixel) >50:
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
    return (pixel[0]+pixel[1]+pixel[2])/3

def showboxplot(dictionary):
    temp = []
    i=0
    keys = list(dictionary.keys())
    while i<len(keys):
        temp.append(dictionary[keys[i]])
        i +=1
    matplotlib.pyplot.show(matplotlib.pyplot.boxplot(temp))

def giveVariance(pixels):
    i = 0
    mean=0
    while i < len(pixels):
        mean += greyscale(pixels[i])
        i+=1
    mean /= len(pixels)
    i = 0
    var = 0
    while i < len(pixels):
        var += math.pow(greyscale(pixels[i])-mean, 2)
        i+=1
    var /= len(pixels)
    return var

