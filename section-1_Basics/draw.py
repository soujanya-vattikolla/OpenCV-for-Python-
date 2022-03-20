import cv2 as cv2

import numpy as np

#creating a blank image
blankimg = np.zeros((500,500,3),dtype="uint8")

cv2.imshow("Blank",blankimg)

# 1. Paint the image a certain colour
blankimg[:] = 0,255,0
cv2.imshow('Green',blankimg)

# 2. Draw a Square
blankimg[200:300, 300:400] = 0,0,255
cv2.imshow('Square',blankimg)

# 2. Draw a Rectangle
cv2.rectangle(blankimg,(0,0), (250,500), (0,255,0), thickness=2)

# fill the rectangle with color
cv2.rectangle(blankimg,(0,0),(250,500),(0,250,0),thickness=cv2.FILLED) 
#or 
cv2.rectangle(blankimg,(0,0),(250,250),(0,250,0),thickness=-1)

cv2.imshow('Rectange', blankimg)

# 3. Draw A circle
cv2.circle(blankimg, (blankimg.shape[0]//2,blankimg.shape[1]//2), 40, (0,0,255), thickness=-1)
cv2.imshow("Circle", blankimg)

# 4. Draw a line
cv2.line(blankimg, (0,0), (blankimg.shape[0]//2,blankimg.shape[1]//2), (255,255,255), thickness=2)
cv2.imshow("Line",blankimg)

# 5. Write text
cv2.putText(blankimg,"Hello", (255,255), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv2.imshow("Line", blankimg)

cv2.waitKey(0)