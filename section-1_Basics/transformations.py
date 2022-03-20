import cv2 as cv2
import numpy as np

img = cv2.imread('../resources/photos/garden.jpg')

cv2.imshow('Garden',img)

#Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv2.imshow("translated img", translated)

# rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv2.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv2.imshow("Rotated img", rotated)

rotated_twice = rotate(img,-45)
cv2.imshow("Rotated twice img", rotated_twice)


# resize
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow("resized image", resized)

# flip
# 0 means flipping image vertically
# 1 means flipping image horizontally
# -1 means flipping image both sides
flipimage = cv2.flip(img, 0)
cv2.imshow("Flipimage", flipimage)

#cropping

cropped = img[200:400,300:400]
cv2.imshow('Cropped',cropped)

cv2.waitKey(0)