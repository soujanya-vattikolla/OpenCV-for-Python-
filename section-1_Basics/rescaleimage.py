import cv2 as cv2

img = cv2.imread('../resources/photos/dog.jpg')

cv2.imshow('Dog',img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

resized_image = rescaleFrame(img)
cv2.imshow('Image',resized_image)
cv2.waitKey(0)
