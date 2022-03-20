import cv2 as cv2
import numpy as np

img = cv2.imread('../resources/photos/cat.jpg')

cv2.imshow('Cat',img)

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow('Blank',blank)

grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',grayimg)

blurimg = cv2.GaussianBlur(grayimg, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur',blurimg)

cannyimg = cv2.Canny(blurimg, 125,175)
cv2.imshow('Canny edge',cannyimg)

ret,thresh = cv2.threshold(grayimg, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh", thresh)

contours, hierarchies = cv2.findContours(cannyimg, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv2.drawContours(blank,contours,-1, (0,0,255), 1)
cv2.imshow('Contours drawn',blank)

cv2.waitKey(0)