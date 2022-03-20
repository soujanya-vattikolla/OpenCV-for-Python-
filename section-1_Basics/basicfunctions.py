import cv2 as cv2

img = cv2.imread('../resources/photos/lady.jpg')

cv2.imshow('Lady', img)

# Converting to gray scale img

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image", grayimg)

# Blur 

blurimg = cv2.GaussianBlur(img, (7,7), cv2.BORDER_DEFAULT)
cv2.imshow("Blurimg",blurimg)

# Edge Cascade

cannyimg = cv2.Canny(blurimg, 125,175)
cv2.imshow("Cannyimg", cannyimg)

# Dilating the image

dilateimg = cv2.dilate(cannyimg, (7,7), iterations=1)
cv2.imshow("Diatedimg",dilateimg)

# Eroding

erodeimg = cv2.erode(dilateimg, (7,7), iterations=1)
cv2.imshow("Erodeimg", erodeimg)

# Resize

resizeimg = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
cv2.imshow("Resizedimage", resizeimg)

# Cropping

cropimg = img[50:200, 200:400]
cv2.imshow("Cropimg", cropimg)

cv2.waitKey(0)