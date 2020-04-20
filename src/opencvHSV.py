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


img = cv2.imread('../images/color_coordinate.png',cv2.IMREAD_COLOR)
# img = cv2.imread('../images/kyoryu.png',cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_array = imgNdarray2ColorNdarray(img)
# とっても重い処理(約３秒くらい)
colorArray, count = np.unique(img_array, return_counts=True, axis=0)
indexMaxcount = np.argmax(count)

print(colorArray[indexMaxcount])
print(cv2.cvtColor(np.array([[colorArray[indexMaxcount]]]), cv2.COLOR_HSV2RGB)[0][0])