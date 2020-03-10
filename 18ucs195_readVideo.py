# ASSIGNMENT 0
# READ VIDEO
# Raghav Chugh     18UCS195
# Lakshay Bhagtani 18UCS132
import cv2
import sys

if len(sys.argv)>1:
    fileName = sys.argv[0]
else:
    fileName = "video1.mp4"

# Create window to display video frames
cv2.namedWindow("video",cv2.WINDOW_AUTOSIZE)

# Read Video File
cap = cv2.VideoCapture(0)
cap.open(fileName)

numFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("Number of frames ",numFrames)
print("Dimensions of each frame ",frameWidth,", ",frameHeight)

while 1 :
    # Capture frame-by-frame
    ret, frame = cap.read()


    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 27:
        sys.exit()

destroyWindow("video");
cap.release();
