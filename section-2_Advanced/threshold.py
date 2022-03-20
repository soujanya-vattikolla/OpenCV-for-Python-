import cv2 as cv2
from cv2 import threshold

img = cv2.imread('../resources/photos/dog.jpg')

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',grayimg)

# Simple Thresholding
threshold,thresh = cv2.threshold(grayimg, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Simple Threshold', thresh)

threshold,thresh_inv = cv2.threshold(grayimg, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Simple Threshold Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(grayimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 5)
cv2.imshow('Adaptive Thresholding', adaptive_thresh)

cv2.waitKey(0)