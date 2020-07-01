import cv2
import numpy as np

img = cv2.imread('me.jpg')
img = cv2.resize(img, (500,500))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray, (3,3), 0)

kernelX = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
kernelY = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

img_prewittX = cv2.filter2D(img_gaussian, -1, kernelX)
img_prewittY = cv2.filter2D(img_gaussian, -1, kernelY)

cv2.imshow("Prewitt Vertical Filter", img_prewittX)
cv2.imshow("Prewitt Horizontal Filter", img_prewittY)

cv2.waitKey(0)
cv2.destroyAllWindows()