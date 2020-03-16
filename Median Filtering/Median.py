# ASSIGNMENT 1 + ConnectedComponentLabelling + MedianFiltering + DeNoising
# Raghav Chugh     18UCS195
# Lakshay Bhagtani 18UCS132
#Collaborators
#Piyush Soni 18ucs067
#Divyansh Singh 18ucs132
import cv2
import numpy as np

img = cv2.imread('Demo.jpg',1)
filter_size = 3
M,N,G = img.shape
Iter = filter_size // 2
imgnew = np.copy(img)
x = np.pad(img, pad_width=1, mode='constant', constant_values=0)
for X in range(Iter,M-Iter):
    for Y in range(Iter,N-Iter):
        Window = img[X-Iter:X+Iter,Y-Iter:Y+Iter]
        imgnew[X+Iter,Y+Iter] = np.median(Window)
window_name = 'image'
cv2.imshow(window_name,imgnew)
cv2.waitKey(0)
