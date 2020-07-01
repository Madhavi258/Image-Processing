import numpy as np
import cv2
img=cv2.imread('brightness.jpg',0)
out=img.copy()
height=img.shape[0]
width=img.shape[1]
for i in np.arange(4,height-4):
    for j in np.arange(4,width-4):
        sum=0
        for k in np.arange(-5,4):
            for l in np.arange(-5,4):
                a=img.item(i+k,j+l)
                sum=sum+a
            b=int(sum/81.0)
            out.itemset((i,j),b)
cv2.imwrite('box_filter.jpg',out)
cv2.imshow('Blurred',out)
cv2.waitKey(0)