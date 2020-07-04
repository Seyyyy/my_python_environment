import numpy as np
import cv2

img = np.zeros((480,120,3), np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# hue * 15
img[0:40, 0:40] = [0,255,255] #0
img[40:80, 0:40] = [15,255,255] #1
img[80:120, 0:40] = [30,255,255] #2
img[120:160, 0:40] = [45,255,255] #3
img[160:200, 0:40] = [60,255,255] #4
img[200:240, 0:40] = [75,255,255] #5
img[240:280, 0:40] = [90,255,255] #6
img[280:320, 0:40] = [105,255,255] #7
img[320:360, 0:40] = [120,255,255] #8
img[360:400, 0:40] = [135,255,255] #9
img[400:440, 0:40] = [150,255,255] #10
img[440:480, 0:40] = [165,255,255] #11

# floor(saturation * 21.33)
img[0:40, 40:80] = [0,0,255] #0
img[40:80, 40:80] = [0,21,255] #1
img[80:120, 40:80] = [0,43,255] #2
img[120:160, 40:80] = [0,64,255] #3
img[160:200, 40:80] = [0,85,255] #4
img[200:240, 40:80] = [0,107,255] #5
img[240:280, 40:80] = [0,128,255] #6
img[280:320, 40:80] = [0,149,255] #7
img[320:360, 40:80] = [0,171,255] #8
img[360:400, 40:80] = [0,192,255] #9
img[400:440, 40:80] = [0,213,255] #10
img[440:480, 40:80] = [0,235,255] #11

# floor(value * 21.33)
img[0:40, 80:120] = [0,0,0] #0
img[40:80, 80:120] = [0,0,21] #1
img[80:120, 80:120] = [0,0,43] #2
img[120:160, 80:120] = [0,0,64] #3
img[160:200, 80:120] = [0,0,85] #4
img[200:240, 80:120] = [0,0,107] #5
img[240:280, 80:120] = [0,0,128] #6
img[280:320, 80:120] = [0,0,149] #7
img[320:360, 80:120] = [0,0,171] #8
img[360:400, 80:120] = [0,0,192] #9
img[400:440, 80:120] = [0,0,213] #10
img[440:480, 80:120] = [0,0,235] #11
img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
cv2.imwrite('../images/color.png', img)