import cv2 as cv2
from cv2 import COLOR_BGR2Lab
from cv2 import COLOR_BGR2LAB
import matplotlib.pyplot as plt

img = cv2.imread('../resources/photos/park.jpg')

cv2.imshow("Park",img)

# BGR to Gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayimage",gray)

#BGR to HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',hsv)

#BGR to lab
lab = cv2.cvtColor(img,COLOR_BGR2LAB)
cv2.imshow("lab",lab)

# plot image
plt.imshow(img)
plt.show()

#BGR to RGB
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("RGB",rgb)

#hSV to BGR
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_BGR2RGB)
cv2.imshow("HSV----BGR", hsv_bgr)

cv2.waitKey(0)