# ASSIGNMENT 0
# WRITE IMAGE
# Raghav Chugh     18UCS195
# Lakshay Bhagtani 18UCS132

import cv2
import sys
img = cv2.imread("./lena_color.tif", cv2.IMREAD_GRAYSCALE) #read the image data in the file "lena_color.tif" and store it in 'img'
# IMREAD_COLOR
# IMREAD_GRAYSCALE

#check whether the image is loaded or not
if img is None:
	print("Error : Image cannot be loaded..!!")
	sys.exit()

#	namedWindow("MyWindow", WINDOW_NORMAL) #create a window with the name "MyWindow"
cv2.namedWindow("MyWindow", cv2.WINDOW_AUTOSIZE) #create a window with the name "MyWindow"
cv2.imshow("MyWindow", img) #display the image which is stored in the 'img' on the "MyWindow" window

cv2.waitKey(0) #wait infinite time for a keypress
#	imwrite("img.png", img); //function to save image

cv2.destroyWindow("MyWindow") #destroy the window with the name, "MyWindow"

cv2.imwrite("lena_gray.png",img)
