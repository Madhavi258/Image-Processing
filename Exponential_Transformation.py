import numpy as np
import cv2
import math
img=cv2.imread('brightness.jpg',0)
cv2.imshow('original',img)
height=img.shape[0]
width=img.shape[1]
for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        c=(255/(1.01**255)-1)
        b=c*((1.01**a)-1)
        img.itemset((i,j),b)
cv2.imwrite('Exponential_Transformation.jpg',img)
cv2.imshow('Transformed',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
cv2.destroyAllWindows()