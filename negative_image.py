import numpy as np
import cv2
import math
img=cv2.imread('me.jpg',0)
cv2.imshow('img1',img)
height=img.shape[0]
width=img.shape[1]
max_intensity=255
for i in np.arange(height):
    for j in np.arange(width):
        a=img.item(i,j)
        b=max_intensity-a
        if b>255:
            b=255
        img.itemset((i,j),b)
cv2.imwrite('negative.jpg',img)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
cv2.destroyAllWindows()