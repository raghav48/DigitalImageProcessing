import numpy as np
import cv2

image = cv2.imread("Demo.jpg",0)
cv2.imshow("original",image)
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

image = np.array(c)
image = image/255

cv2.imshow("imagenew",image)
cv2.waitKey(0)
cv2.destroyAllWindows()