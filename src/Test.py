from numpy import *
import pandas as pd
from PIL import Image
from copy import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

from DataFrame import *
from Confusion import calcAccuracy
from FileIO import *
from Process import *
import pickle


## Self contained, but you have to change the target number in Process.py under genLogModel
def tester():
    exact = "../../fake_microstructure/Target_1/p2mask_np_0.png"

    exactArr = readGraynne(exact)
    exactList = []
    for i in range(exactArr.size):
        if(exactArr[i]>30000):
            exactList.append(1)
        else:
            exactList.append(0)
    sum = 0
    for i in range(len(exactList)):
        if(exactList[i] == 0):
            sum = sum + 1
    exactFrac = sum/(len(exactList))
    return exactFrac
