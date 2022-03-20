import cv2 as cv

# Read in an image
img = cv.imread('photos/cat.jpg')

# display the image by using imshow method
cv.imshow('Cat',img)

# waits for specific delay for the key to be pressed
cv.waitKey(0)

