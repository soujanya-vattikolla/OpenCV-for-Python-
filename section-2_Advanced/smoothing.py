import cv2 as cv2

img = cv2.imread('../resources/photos/cat.jpg')

cv2.imshow("Cat",img)

#Averaging
average = cv2.blur(img, (7,7))
cv2.imshow('Average Blur', average)

#GaussianBlur
gaussian = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('Gaussian Blur', gaussian)

#MedianBlur
median = cv2.medianBlur(img,7)
cv2.imshow('Median Blur', median)

#bilateral
bilateral = cv2.bilateralFilter(img, 10, 15,15)
cv2.imshow('Bilateral Blur',bilateral)

cv2.waitKey(0)