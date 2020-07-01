import cv2
from matplotlib import pyplot as plt
img1=cv2.imread('me.jpg',-1)
img2=cv2.imread('me2.jpg',-1)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#cv2.imshow('img1',gray1)
#cv2.imshow('img2',gray2)
plt.hist(gray1.ravel(),256,[0,256]);
plt.show()
plt.hist(gray2.ravel(),256,[0,256]);
plt.show()
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
cv2.destroyAllWindows()
