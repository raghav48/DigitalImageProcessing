# ASSIGNMENT 0
# KEYBOARD HANDLER
# Raghav Chugh     18UCS195
# Lakshay Bhagtani 18UCS132
import cv2
import sys
import numpy as np

if len(sys.argv)>1:
    fileName = sys.argv[0]
else:
    fileName = "lena_color.tif"

# Load Image
image = cv2.imread(fileName,cv2.IMREAD_UNCHANGED);

#check whether the image is loaded or not
if image is None:
    sys.exit("Error : Image cannot be loaded..!!")
print(image.shape)
height,width,cols = image.shape

# Create new images

#convert colored image to gray scale
grayScaleImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# binarize the grayscale image
thresh,binaryImage = cv2.threshold(grayScaleImage, 128, 255, cv2.THRESH_BINARY)

# resize image
smallImage = cv2.resize(image, None , 0.5, 0.5, cv2.INTER_LINEAR)
#	resize(image, smallImage, Size(width/2, height/2), INTER_LINEAR);

#display original image
cv2.namedWindow("image",cv2.WINDOW_AUTOSIZE)

print("Press \n 'i' to display original image \n 'g' for grayscale \n 'b' for binary, \n 's' for smaller sized image and 'Esc' to exit")
cv2.imshow("image", image)

while 1:
    #wait for keyboard input
    key = cv2.waitKey(0)
    # press 'Esc' to quit the program
    if key==27:
        sys.exit()
    # 'g' pressed, display the grayscale image
    if chr(key)=='g':
        cv2.imshow("image", grayScaleImage)
    # 'b' pressed, display the binarized image
    if chr(key)=='b':
        cv2.imshow("image", binaryImage)
    # 's' pressed, display the resized smaller image
    if chr(key)=='s':
        cv2.imshow("image", smallImage)
    if chr(key)=='i':
        cv2.imshow("image", image)
#free memory
cv2.destroyWindow("image")
