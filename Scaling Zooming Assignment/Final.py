# ASSIGNMENT 0
# READ PIXEL
# Raghav Chugh     18UCS195
# Lakshay Bhagtani 18UCS132
import cv2
import numpy as np
# Read an image, a window and bind the function to window

def ScaleImage(image):
    a = list(image)
    b = []
    m = 5
    l = len(a)
    t=0
    for i in range(0,l,m):
        f = []
        for v in range(0,l,m):
            f.append(a[i][v])
        b.append(f)
    b=np.array(b)
    b=b/255
    ScaledImage = b
    cv2.imshow("Scaled",ScaledImage)
    cv2.waitKey(0)
def RepititionImage(image):
    row = image.shape[0]
    columns = image.shape[1]
    resize = 2
    imagenew = np.zeros((row * resize, columns * resize))
    for r in range(row):
        startr = r * resize
        for c in range(columns):
            startc = c * resize
            imagenew[startr:startr + resize, startc:startc + resize] = np.ones((resize, resize),dtype=np.int) * image[r, c]
    imagenew=np.array(imagenew/255)
    cv2.imshow("RepititionImage",imagenew)
    cv2.waitKey(0)
def InterpolateImage(image):
    a = list(image)
    b = []
    le = len(a)
    for i in range(1,le-1):
        f = []
        for v in range(1,le-1):
            f.append(a[i][v])
            t = ( int(a[i][v]) + int(a[i][v+1]) ) / 2
            f.append(t)
        b.append(f)
    c = []
    b.append([0]*len(b[0]))
    for i in range(len(b)-1):
        c.append(b[i])
        f = []
        for v in range(len(b[i])):
            g = ( int(b[i][v]) + int(b[i+1][v]) ) / 2
            f.append(g)
        c.append(f)
    interpolatedImage = np.array(c)
    interpolatedImage = interpolatedImage/255
    cv2.imshow("InterpolatedImage",interpolatedImage)
    cv2.waitKey(0)
# def mouseHandler(event,x,y,flags,param):
    # img1 = image.copy()
    # if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        # print("X: ",x,"Y: ",y)



image = cv2.imread("grey.png",0)
cv2.imshow('Image',image)
cv2.waitKey(0)
ScaleImage(image)
RepititionImage(image)
InterpolateImage(image)
#Do until esc pressed
while(1):
    if cv2.waitKey(20) & 0xFF == 27:
        break
#if esc pressed, finish.
cv2.destroyAllWindows()
