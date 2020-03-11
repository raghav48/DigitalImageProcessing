import cv2
import numpy as np

row=4
columns=4
channels=1
resize=3
image = cv2.imread("Demo.jpg")
imagenew=np.zeros((row*resize,columns*resize,3))
for r in range(row):
    startr=r*resize
    for c in range(columns):
        startc=c*resize
        imagenew[startr:startr+resize,startc:startc+resize]=np.ones((resize,resize))*image[r,c]

cv2.imshow("MyWindow", res)
