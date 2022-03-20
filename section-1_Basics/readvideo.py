import cv2 as cv

# reading videos

capture = cv.VideoCapture('../resources/videos/dog.mp4')

# reading video frame by frame

while True:
    isTrue, frame = capture.read()

    # display video
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()