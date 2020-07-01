import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('me.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (500,500))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
cv2.imshow('Sobel Horizontal Filter',sobelX)
cv2.imshow('Sobel Vertical Filter',sobelY)
cv2.waitKey(0)
cv2.destroyAllWindows()