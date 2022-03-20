import cv2 as cv2
import numpy as np

img = cv2.imread('../resources/photos/cat2.jpg')
cv2.imshow("Cat",img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Blank image",blank)

mask_circle = cv2.circle(blank.copy(), (img.shape[1]//2+45, img.shape[0]//2), 100, 255, -1)
cv2.imshow("Mask",mask_circle)

mask_rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

masked = cv2.bitwise_and(img,img,mask=mask_circle)
cv2.imshow("Masked image",masked)

new_shape = cv2.bitwise_and(mask_circle,mask_rectangle)
cv2.imshow('New shape',new_shape)

masked_newshape = cv2.bitwise_and(img,img,mask=new_shape)
cv2.imshow('New Shaped Masked Image', masked_newshape)

cv2.waitKey(0)