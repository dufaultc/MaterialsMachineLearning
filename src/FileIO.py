## ReadGraynne Module
#  Reads image info for Graynne program
#  Entry for DeltaHacks V
#  Tim Choy, Sam Crawford, Lewis Rafuse, and Cameron Dufault

from copy import *
from math import sqrt

from numpy import *
from PIL import Image

## Function readGraynne
#  Parameter image_name: string of name of image file
#  Description: Takes a string of the name of image and returns a 2D array of
#  grayscale values of the image. Grayscale pixel value ranges from 0 to 255
def readGraynne(image_name):
    img = Image.open(image_name, 'r').convert('I')
    data = asarray(img)
    data = reshape(data, 1048576)
    return data

## Function writeGraynne
#  Parameter data: a numpy 1D array
#  Description: Takes in a 1D numpy array and turns it into a 2D array, and
#  outputs a .png file named output.png.
def writeGraynne(data):
    # data is read-only, so we create a tmp
    tmp = []
    sum = 0
    for i in range(len(data)):
        if(data[i] == 1):
            tmp.append(65535)
        else:
            sum += 1
            tmp.append(0)
    #data2D = reshape(tmp, (-1, int(sqrt(data.size))))
    tmp2D = [tmp[i:i+1024] for i in range(0, len(tmp), 1024)]
    data2D = array(tmp2D)
    #print(tmp)
    #print(type(tmp[0]))
    #print(data2D)
    img = Image.fromarray(data2D, "I")
    img.save("output.png")

    return sum / 1048576
