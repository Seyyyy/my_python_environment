import numpy as np
import cv2

# np.uniqueで使用されるカラーリストを抽出するための前処理
def imgNdarray2ColorNdarray(imgNdarray):
    img_array = []
    for cell in img:
        for row in cell:
            img_array.append(row)
    img_array = np.array(img_array)
    return img_array

# 取得画像のベースカラーに対する補色を取得
def getNuanceColor(baseColor, colorArray):
    nuance = []
    stack = 100
    baseColorSum = baseColor.max() + baseColor.min()
    compColor = [
        baseColorSum - baseColor[0], 
        baseColorSum - baseColor[1],
        baseColorSum - baseColor[2]]
    for color in colorArray:
        temp = color - compColor
        temp = np.abs(temp)
        avg = np.mean(temp)
        if(stack > temp).any():
            stack = temp
            nuance = color
    return nuance

img = cv2.imread('../images/color_coordinate.png',cv2.IMREAD_COLOR)
# img = cv2.imread('../images/kyoryu.png',cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_array = imgNdarray2ColorNdarray(img)
# とっても重い処理(約３秒くらい)
colorArray, count = np.unique(img_array, return_counts=True, axis=0)
# 面積のでかいベースカラー
indexMaxcount = np.argmax(count)

nuance = getNuanceColor(baseColor=colorArray[indexMaxcount], colorArray=colorArray)

print(colorArray.size)
print(indexMaxcount)
print(colorArray[indexMaxcount])
print(nuance)