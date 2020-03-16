# ASSIGNMENT 1 + ConnectedComponentLabelling + MedianFiltering + DeNoising
# Raghav Chugh     18UCS195
# Lakshay Bhagtani 18UCS132
import cv2
import numpy as np

img = np.array([[1, 1 ,0, 1, 1, 1, 0, 1],
 [1, 1, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 1, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 0, 1, 0 ,1],
 [0, 0, 0, 1, 0, 1, 0 ,1],
 [1, 1, 1, 1, 0, 0, 0 ,1],
 [1, 1, 1, 1, 0, 1, 1 ,1]])


M,N = img.shape

img[0,0] = 1
EquivalencyList = []
K=0
for i in range(M):
    for j in range(N):
        if img[i,j]==1:
            Y = img[i-1,j]
            X = img[i,j-1]
            if i == 0:
                Y=0
            if j == 0:
                X=0
            if X!=0 and Y!=0:
                img[i,j] = min(X,Y)
                EquivalencyList.append((X,Y))
            elif X!=0 and Y==0:
                img[i,j] = X
            elif X==0 and Y!=0:
                img[i,j] = Y
            elif X==0 and Y==0:
                K=K+1
                img[i,j] = K
print("Image\n" ,img)
print("Equivalency List\n",EquivalencyList)

for i,j in EquivalencyList:
    if i!=j:
        for x in range(M):
            for y in range(N):
                if img[x,y] == i:
                    img[x,y] = min(i,j)

print("Final Image\n",img)
