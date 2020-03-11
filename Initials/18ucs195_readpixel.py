# ASSIGNMENT 0
# READ PIXEL
# Raghav Chugh     18UCS195
# Lakshay Bhagtani 18UCS132
import cv2
import numpy as np


def mouseHandler(event,x,y,flags,param):
    label = "Tutorial"
    img1 = image.copy()
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = image[y,x,0]
        colorsG = image[y,x,1]
        colorsR = image[y,x,2]
        colors = image[y,x]
        print(colors)
        print("X: ",x,"Y: ",y)
        cv2.rectangle(img1,(x,y-12),(x+100,y+4),(0,0,255),-1)
        cv2.putText(img1,label,(x, y),cv2.FONT_HERSHEY_PLAIN,0.5,(255,255,0))
        cv2.imwrite("test.png",img1)

# Read an image, a window and bind the function to window
image = cv2.imread("lena_color.tif")
cv2.namedWindow('Image')
cv2.setMouseCallback('Image',mouseHandler)
cv2.imshow('Image',image)

#Do until esc pressed
while(1):
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.
cv2.destroyAllWindows()
