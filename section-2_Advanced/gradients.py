import cv2 as cv2
import numpy as np

img = cv2.imread('../resources/photos/park.jpg')
cv2.imshow('Park Image',img)

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image',grayimg)

# Laplacian
lap = cv2.Laplacian(grayimg, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian', lap)

# Sobel 
sobelx = cv2.Sobel(grayimg, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(grayimg, cv2.CV_64F, 0, 1)
combined_sobel = cv2.bitwise_or(sobelx, sobely)

cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Combined Sobel', combined_sobel)


canny = cv2.Canny(grayimg, 150, 175)
cv2.imshow('Canny', canny)

cv2.waitKey(0)