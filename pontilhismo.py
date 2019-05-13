import cv2
import numpy as np
from copy import copy
import random

STEP = 5
JITTER = 3
RAIO = 3

image = cv2.imread("lenna.png", 0)
height, width = image.shape
points = copy(image)

for i in range(height):
    for j in range(width):
        points[i, j] = 255

xrange = np.zeros(int(height/STEP))
yrange = np.zeros(int(width/STEP))

for xvalue in range(len(xrange)):
    xrange[xvalue] = xvalue

for yvalue in range(len(yrange)):
    yrange[yvalue] = yvalue

xrange = [value*STEP+STEP/2 for value in xrange]
yrange= [value*STEP+STEP/2 for value in yrange]

np.random.shuffle(xrange)

for i in xrange:
    np.random.shuffle(yrange)
    for j in yrange:
        x = int(i + random.randint(1, 2*JITTER-JITTER))
        y = int(j + random.randint(1, 2*JITTER-JITTER))
        if(x >= height):
                x = height-1
        if( y >= width):
                y = width-1
        gray = image[x,y]
        cv2.circle(points,
                (y, x),
                RAIO,
                int(gray),
                -1,
                cv2.LINE_AA)

cv2.imwrite("pontos.png", points)
cv2.imshow("pontos", points)
cv2.waitKey(0)     
cv2.destroyAllWindows()
