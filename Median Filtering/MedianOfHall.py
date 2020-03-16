# ASSIGNMENT 1 + ConnectedComponentLabelling + MedianFiltering + DeNoising
# Raghav Chugh     18UCS195
# Lakshay Bhagtani 18UCS132
#Collaborators
#Piyush Soni 18ucs067
#Divyansh Singh 18ucs132
import cv2
import numpy as np


img=cv2.imread('img3.JPG',cv2.IMREAD_GRAYSCALE)
imagearray=list()

for x in range(0,28):

    image=cv2.imread('img'+str(x)+'.JPG',cv2.IMREAD_GRAYSCALE)

    imagearray.append(image)
imagearray=np.array(imagearray)
shape = imagearray.shape
print(shape)
number = shape[0]
rows = shape[1]
col = shape[2]
newimage=np.zeros((400,600))
for r in range(rows):
    for c in range(col):
        values=imagearray[:,r,c]
        newimage[r,c]=np.median(values)





newimage=newimage/255
cv2.imshow('image',newimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
