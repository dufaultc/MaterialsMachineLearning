# diffs.py

from numpy import *
import pandas as pd
from PIL import Image
from copy import *

def threeUp(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*3):
        diff[i] = 0
    for i in range(1024*3, len(readRGB)):
        diff[i] =  readRGB[i] - readRGB[i - 3*1024]

    return diff

def threeDown(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*(1024-3)):
        diff[i] = readRGB[i] - readRGB[i + 3*1024]
    for i in range(1024*(1024-3), len(readRGB)):
        diff[i] = 0

    return diff

def threeRight(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 < 1021):
            diff[i] = readRGB[i] - readRGB[i + 3]
        else:
            diff[i] = 0

    return diff

def threeLeft(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 > 2):
            diff[i] = readRGB[i] - readRGB[i - 3]
        else:
            diff[i] = 0

    return diff

def fiveUp(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*5):
        diff[i] = 0
    for i in range(1024*5, len(readRGB)):
        diff[i] =  readRGB[i] - readRGB[i - 5*1024]

    return diff


def fiveDown(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*(1024-5)):
        diff[i] = readRGB[i] - readRGB[i + 5*1024]
    for i in range(1024*(1024-5), len(readRGB)):
        diff[i] = 0

    return diff

def fiveRight(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 < 1019):
            diff[i] = readRGB[i] - readRGB[i + 5]
        else:
            diff[i] = 0

    return diff

def fiveLeft(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 > 4):
            diff[i] = readRGB[i] - readRGB[i - 5]
        else:
            diff[i] = 0

    return diff
def sevenUp(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*7):
        diff[i] = 0
    for i in range(1024*7, len(readRGB)):
        diff[i] =  readRGB[i] - readRGB[i - 7*1024]

    return diff
def sevenDown(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*(1024-7)):
        diff[i] = readRGB[i] - readRGB[i + 7*1024]
    for i in range(1024*(1024-7), len(readRGB)):
        diff[i] = 0

    return diff

def sevenRight(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 < 1017):
            diff[i] = readRGB[i] - readRGB[i + 7]
        else:
            diff[i] = 0

    return diff

def sevenLeft(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 > 6):
            diff[i] = readRGB[i] - readRGB[i - 7]
        else:
            diff[i] = 0

    return diff



def tenUp(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*10):
        diff[i] = 0
    for i in range(1024*10, len(readRGB)):
        diff[i] =  readRGB[i] - readRGB[i - 10*1024]

    return diff

def tenDown(readRGB):
    diff = empty(len(readRGB))
    for i in range(1024*(1024-10)):
        diff[i] = readRGB[i] - readRGB[i + 10*1024]
    for i in range(1024*(1024-10), len(readRGB)):
        diff[i] = 0

    return diff

def tenRight(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 < 1014):
            diff[i] = readRGB[i] - readRGB[i + 10]
        else:
            diff[i] = 0

    return diff

def tenLeft(readRGB):
    diff = empty(len(readRGB))
    for i in range(len(readRGB)):
        if (i % 1024 > 9):
            diff[i] = readRGB[i] - readRGB[i - 10]
        else:
            diff[i] = 0

    return diff
