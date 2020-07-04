import numpy as np
import cv2
import math
import csv
import glob

# np.uniqueで使用されるカラーリストを抽出するための前処理
def imgNdarray2ColorNdarray(imgNdarray):
    img_array = []
    for cell in imgNdarray:
        for row in cell:
            img_array.append(row)
    img_array = np.array(img_array)
    return img_array

# hsvだと色数が多すぎるので扱いやすくするために抽象化をする
def abstraction(imgNdarray):
    img_array = []
    abstParam = [15, 18.2, 18.2]
    img_array = np.floor(imgNdarray / abstParam)
    img_array = img_array.astype(np.int64)
    return img_array


def hueAbs(hueNdarray):
    img_array = []
    for value in hueNdarray:
        if not ((value[1] < 5 and value[2] < 5) and (value[1] > 250 and value[2] > 250)):
            img_array.append(value[0])
    return img_array


def satuAbs(satuNdarray):
    img_array = []
    for value in satuNdarray:
        if not (value[2] < 5 and value[2] > 250):
            img_array.append(value[1])
    return img_array


def valueAbs(valueNdarray):
    img_array = []
    for value in valueNdarray:
        if not (value[1] < 5 and value[1] > 250):
            img_array.append(value[2])
    return img_array

# とっても重い処理(約３秒くらい)uniqueが重たいたぶん
# 色相、彩度、明度ごとに割合を導出する
def getColorFeature(uniqueColorNdarray):
    hue, hueCount = np.unique(uniqueColorNdarray[0], return_counts=True)
    saturation, satuCount = np.unique(uniqueColorNdarray[1], return_counts=True)
    value, valueCount = np.unique(uniqueColorNdarray[2], return_counts=True)
    hueRatio = fillZero(hue, colorRatio(hueCount))
    satuRatio = fillZero(saturation, colorRatio(satuCount))
    valueRatio = fillZero(value, colorRatio(valueCount))
    ratio = [hueRatio, satuRatio, valueRatio]
    return ratio

def colorRatio(colorCountNdarray):
    ratio = np.round(colorCountNdarray / colorCountNdarray.sum(), 3)
    return ratio

# csvで扱いやすくするために列と対応させるように０で埋める
def fillZero(colorKindNdarray, colorRatioNdarray):
    abstractionNumber = 12
    ratioArray = np.zeros(abstractionNumber)
    for i, colorNumber in enumerate(colorKindNdarray):
        ratioArray[colorNumber] = colorRatioNdarray[i]
    return ratioArray

def getEntropy(ratioNdarray):
    H = 0
    for ratio in ratioNdarray:
        if ratio == 0:
            continue
        H -= ratio * math.log2(ratio)
    return H

# とりあえず繰り返し処理しやすいようにまとめる
def mainFunction(imageFileName):
    img = cv2.imread(imageFileName, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_array = imgNdarray2ColorNdarray(img)
    img_array = abstraction(img_array)
    # Hue, Saturation, Valueをまとめた２次元配列
    # uniqueColorArray = img_array.T
    uniqueColorArray = [hueAbs(img_array), satuAbs(img_array), valueAbs(img_array)]
    print(uniqueColorArray)
    hsvColorKind = getColorFeature(uniqueColorArray)
    # エントロピー用の配列を作る
    hueEntropy = getEntropy(hsvColorKind[0])
    satuEntropy = getEntropy(hsvColorKind[1])
    valueEntropy = getEntropy(hsvColorKind[2])
    entropy = [hueEntropy, satuEntropy, valueEntropy]
    #１次元配列に平滑化（もっといい方法あると思う）
    csvArray = np.append(hsvColorKind[0], hsvColorKind[1])
    csvArray = np.append(csvArray, hsvColorKind[2])
    csvArray = np.append(csvArray, entropy)
    # with open('../data/color.csv', 'a') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(csvArray)

# 最初の一回だけheaderを記入
# with open('../data/color.csv', 'w') as f:
#     fieldNames = [
#         'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11',
#         's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11',
#         'v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8',  'v9', 'v10', 'v11', 
#         'hue entropy', 'saturation entropy', 'value entropy'
#     ]
#     writer = csv.DictWriter(f, fieldnames=fieldNames)
#     writer.writeheader()

# images = glob.glob('../sampledata/*')
# for path in images:
#     mainFunction(path)

mainFunction('../images/kyoryu.png')

# print(cv2.cvtColor(np.array([[colorArray[indexMaxcount]]]), cv2.COLOR_HSV2RGB)[0][0])