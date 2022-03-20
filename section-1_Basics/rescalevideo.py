import cv2 as cv2

# resizing the video
def rescaleFrame(frame, scale=0.75):
    # Images, Videos and live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

# change the resolution in live videos(webcam)
#def changeRes(width,height):
#    capture.set(3,width)
#    capture.set(4,height)

capture = cv2.VideoCapture('../resources/videos/dog.mp4')

# reading video frame by frame

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    
    cv2.imshow('Video',frame) # original video
    cv2.imshow('Video Resized',frame_resized)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv2.destroyAllWindows()