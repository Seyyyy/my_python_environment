import numpy as np
# import cv2 as cv

print(np.__version__)
# print(cv.__version__)
print('hello world')

array1 = np.array([4, 5, 20])
array2 = np.array([7, 20, 3])

l2norm = np.linalg.norm(array1 - array2)

print(l2norm)