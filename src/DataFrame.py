# DataFrame.py
# Work for handling DataFrames

from pandas import DataFrame

from DiffCalc import *

def genDataFrame(readRGB, mask):
    pixels_dict = {}
    pixelsFrame = DataFrame(pixels_dict)

    pixelsFrame['originalRGB'] = readRGB
    pixelsFrame['Mask']        = mask

    # Convention for order: up, left, right, down

    pixelsFrame['diffThreeUp']    = threeUp(readRGB)
    pixelsFrame['diffFiveUp']     = fiveUp(readRGB)
    pixelsFrame['diffSevenUp']    = sevenUp(readRGB)
    pixelsFrame['diffTenUp']      = tenUp(readRGB)
    pixelsFrame['diffThreeLeft']  = threeLeft(readRGB)
    pixelsFrame['diffFiveLeft']   = fiveLeft(readRGB)
    pixelsFrame['diffSevenLeft']  = sevenLeft(readRGB)
    pixelsFrame['diffTenLeft']    = tenLeft(readRGB)
    pixelsFrame['diffThreeRight'] = threeRight(readRGB)
    pixelsFrame['diffFiveRight']  = fiveRight(readRGB)
    pixelsFrame['diffSevenRight'] = sevenRight(readRGB)
    pixelsFrame['diffTenRight']   = tenRight(readRGB)
    pixelsFrame['diffThreeDown']  = threeDown(readRGB)
    pixelsFrame['diffFiveDown']   = fiveDown(readRGB)
    pixelsFrame['diffSevenDown']  = sevenDown(readRGB)
    pixelsFrame['diffTenDown']    = tenDown(readRGB)

    pixelsFrame['diffThreeUp'].fillna(pixelsFrame['diffThreeUp'].mean(), inplace = True)
    pixelsFrame['diffFiveUp'].fillna(pixelsFrame['diffFiveUp'].mean(), inplace = True)
    pixelsFrame['diffSevenUp'].fillna(pixelsFrame['diffSevenUp'].mean(), inplace = True)
    pixelsFrame['diffTenUp'].fillna(pixelsFrame['diffTenUp'].mean(), inplace = True)
    pixelsFrame['diffThreeLeft'].fillna(pixelsFrame['diffThreeLeft'].mean(), inplace = True)
    pixelsFrame['diffFiveLeft'].fillna(pixelsFrame['diffFiveLeft'].mean(), inplace = True)
    pixelsFrame['diffSevenLeft'].fillna(pixelsFrame['diffSevenLeft'].mean(), inplace = True)
    pixelsFrame['diffTenLeft'].fillna(pixelsFrame['diffTenLeft'].mean(), inplace = True)
    pixelsFrame['diffThreeRight'].fillna(pixelsFrame['diffThreeRight'].mean(),inplace = True)
    pixelsFrame['diffFiveRight'].fillna(pixelsFrame['diffFiveRight'].mean(),inplace = True)
    pixelsFrame['diffSevenRight'].fillna(pixelsFrame['diffSevenRight'].mean(), inplace = True)
    pixelsFrame['diffTenRight'].fillna(pixelsFrame['diffTenRight'].mean(), inplace = True)
    pixelsFrame['diffThreeDown'].fillna(pixelsFrame['diffThreeDown'].mean(), inplace= True)
    pixelsFrame['diffFiveDown'].fillna(pixelsFrame['diffFiveDown'].mean(), inplace= True)
    pixelsFrame['diffSevenDown'].fillna(pixelsFrame['diffSevenDown'].mean(), inplace = True)
    pixelsFrame['diffTenDown'].fillna(pixelsFrame['diffTenDown'].mean(), inplace = True)

    pixelsFrame["Mask"] = pixelsFrame["Mask"].apply(category)

    pixelsFrame["diffThreeUp"]    = pixelsFrame["diffThreeUp"].apply(categoryYo)
    pixelsFrame["diffFiveUp"]     = pixelsFrame["diffFiveUp"].apply(categoryYo)
    pixelsFrame["diffSevenUp"]    = pixelsFrame["diffSevenUp"].apply(categoryYo)
    pixelsFrame["diffTenUp"]      = pixelsFrame["diffTenUp"].apply(categoryYo)
    pixelsFrame["diffThreeLeft"]  = pixelsFrame["diffThreeLeft"].apply(categoryYo)
    pixelsFrame["diffFiveLeft"]   = pixelsFrame["diffFiveLeft"].apply(categoryYo)
    pixelsFrame["diffSevenLeft"]  = pixelsFrame["diffSevenLeft"].apply(categoryYo)
    pixelsFrame["diffTenLeft"]    = pixelsFrame["diffTenLeft"].apply(categoryYo)
    pixelsFrame["diffThreeRight"] = pixelsFrame["diffThreeRight"].apply(categoryYo)
    pixelsFrame["diffFiveRight"]  = pixelsFrame["diffFiveRight"].apply(categoryYo)
    pixelsFrame["diffSevenRight"] = pixelsFrame["diffSevenRight"].apply(categoryYo)
    pixelsFrame["diffTenRight"]   = pixelsFrame["diffTenRight"].apply(categoryYo)
    pixelsFrame["diffThreeDown"]  = pixelsFrame["diffThreeDown"].apply(categoryYo)
    pixelsFrame["diffFiveDown"]   = pixelsFrame["diffFiveDown"].apply(categoryYo)
    pixelsFrame["diffSevenDown"]  = pixelsFrame["diffSevenDown"].apply(categoryYo)
    pixelsFrame["diffTenDown"]    = pixelsFrame["diffTenDown"].apply(categoryYo)

    return pixelsFrame

def genImageDataFrame(readRGB):
    pixels_dict = {}
    pixelsFrame = DataFrame(pixels_dict)

    pixelsFrame['originalRGB'] = readRGB

    pixelsFrame['diffThreeUp']    = threeUp(readRGB)
    pixelsFrame['diffFiveUp']     = fiveUp(readRGB)
    pixelsFrame['diffSevenUp']    = sevenUp(readRGB)
    pixelsFrame['diffTenUp']      = tenUp(readRGB)
    pixelsFrame['diffThreeLeft']  = threeLeft(readRGB)
    pixelsFrame['diffFiveLeft']   = fiveLeft(readRGB)
    pixelsFrame['diffSevenLeft']  = sevenLeft(readRGB)
    pixelsFrame['diffTenLeft']    = tenLeft(readRGB)
    pixelsFrame['diffThreeRight'] = threeRight(readRGB)
    pixelsFrame['diffFiveRight']  = fiveRight(readRGB)
    pixelsFrame['diffSevenRight'] = sevenRight(readRGB)
    pixelsFrame['diffTenRight']   = tenRight(readRGB)
    pixelsFrame['diffThreeDown']  = threeDown(readRGB)
    pixelsFrame['diffFiveDown']   = fiveDown(readRGB)
    pixelsFrame['diffSevenDown']  = sevenDown(readRGB)
    pixelsFrame['diffTenDown']    = tenDown(readRGB)
    
    
    pixelsFrame['diffThreeUp'].fillna(pixelsFrame['diffThreeUp'].mean(), inplace = True)
    pixelsFrame['diffFiveUp'].fillna(pixelsFrame['diffFiveUp'].mean(), inplace = True)
    pixelsFrame['diffSevenUp'].fillna(pixelsFrame['diffSevenUp'].mean(), inplace = True)
    pixelsFrame['diffTenUp'].fillna(pixelsFrame['diffTenUp'].mean(), inplace = True)
    pixelsFrame['diffThreeLeft'].fillna(pixelsFrame['diffThreeLeft'].mean(), inplace = True)
    pixelsFrame['diffFiveLeft'].fillna(pixelsFrame['diffFiveLeft'].mean(), inplace = True)
    pixelsFrame['diffSevenLeft'].fillna(pixelsFrame['diffSevenLeft'].mean(), inplace = True)
    pixelsFrame['diffTenLeft'].fillna(pixelsFrame['diffTenLeft'].mean(), inplace = True)
    pixelsFrame['diffThreeRight'].fillna(pixelsFrame['diffThreeRight'].mean(),inplace = True)
    pixelsFrame['diffFiveRight'].fillna(pixelsFrame['diffFiveRight'].mean(),inplace = True)
    pixelsFrame['diffSevenRight'].fillna(pixelsFrame['diffSevenRight'].mean(), inplace = True)
    pixelsFrame['diffTenRight'].fillna(pixelsFrame['diffTenRight'].mean(), inplace = True)
    pixelsFrame['diffThreeDown'].fillna(pixelsFrame['diffThreeDown'].mean(), inplace= True)
    pixelsFrame['diffFiveDown'].fillna(pixelsFrame['diffFiveDown'].mean(), inplace= True)
    pixelsFrame['diffSevenDown'].fillna(pixelsFrame['diffSevenDown'].mean(), inplace = True)
    pixelsFrame['diffTenDown'].fillna(pixelsFrame['diffTenDown'].mean(), inplace = True)

    pixelsFrame["diffThreeUp"]    = pixelsFrame["diffThreeUp"].apply(categoryYo)
    pixelsFrame["diffFiveUp"]     = pixelsFrame["diffFiveUp"].apply(categoryYo)
    pixelsFrame["diffSevenUp"]    = pixelsFrame["diffSevenUp"].apply(categoryYo)
    pixelsFrame["diffTenUp"]      = pixelsFrame["diffTenUp"].apply(categoryYo)
    pixelsFrame["diffThreeLeft"]  = pixelsFrame["diffThreeLeft"].apply(categoryYo)
    pixelsFrame["diffFiveLeft"]   = pixelsFrame["diffFiveLeft"].apply(categoryYo)
    pixelsFrame["diffSevenLeft"]  = pixelsFrame["diffSevenLeft"].apply(categoryYo)
    pixelsFrame["diffTenLeft"]    = pixelsFrame["diffTenLeft"].apply(categoryYo)
    pixelsFrame["diffThreeRight"] = pixelsFrame["diffThreeRight"].apply(categoryYo)
    pixelsFrame["diffFiveRight"]  = pixelsFrame["diffFiveRight"].apply(categoryYo)
    pixelsFrame["diffSevenRight"] = pixelsFrame["diffSevenRight"].apply(categoryYo)
    pixelsFrame["diffTenRight"]   = pixelsFrame["diffTenRight"].apply(categoryYo)
    pixelsFrame["diffThreeDown"]  = pixelsFrame["diffThreeDown"].apply(categoryYo)
    pixelsFrame["diffFiveDown"]   = pixelsFrame["diffFiveDown"].apply(categoryYo)
    pixelsFrame["diffSevenDown"]  = pixelsFrame["diffSevenDown"].apply(categoryYo)
    pixelsFrame["diffTenDown"]    = pixelsFrame["diffTenDown"].apply(categoryYo)

    return pixelsFrame

def category(data):
    if data > 30000:
        return 1
    else:
        return 0

def categoryYo(data):
    if (data >= -3000 and data <= 3000):
        return 5
    elif (-15000 < data < -3000):
        return 4
    elif (data < -14999):
        return 3
    elif (15000 >= data > 3000):
        return 2
    else:
        return 1
