import cv2
import numpy as np
from copy import copy

l1 = 0
l2 = 0
d = 0
y = 0
delta = 0

image = cv2.imread("praia.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype("float32")
(hue, saturation, value) = cv2.split(image)

saturation = saturation * 1.6
value = value * 1.2

saturation = np.clip(saturation, 0, 255)
value = np.clip(value, 0, 255)

image = cv2.merge([hue, saturation, value])
image = cv2.cvtColor(image.astype("uint8"), cv2.COLOR_HSV2BGR)
image = np.array(image,dtype=np.float32)

#função que define a região de desfoque ao longo do eixo vertical da imagem
def alpha(x, l1, l2, d):
    return (0.5 * (np.tanh((x - l1)/(d + 0.1 )) - np.tanh((x - l2)/(d + 0.1))))

height, width, depth = image.shape

media = np.ones([3,3],dtype=np.float32)
mask = cv2.scaleAdd(media,1/9.0,np.zeros([3,3],dtype=np.float32))
image_2 = copy(image)
for i in range(10):
    image_2 = cv2.filter2D(image_2,-1,mask,anchor=(1,1))

result = np.zeros([height, width, depth])

def sety(l):
    global l1, l2, y, delta
    y = l
    l1 = y - int(delta/2)
    l2 =  y + int(delta/2)
    applyTilt()

def setdelta(l):
    global l1, l2, y, delta
    delta = l
    l1 = y - int(delta/2)
    l2 =  y + int(delta/2)
    applyTilt()

def setd(dv):
    global d
    d = dv
    applyTilt()

def tilt_filter():
    global height, width, l1, l2, d
    array = np.ones([height,width])
    for y in range(height):
        array[y,:] *= alpha(y, l1, l2, d)
    return np.array(array, dtype=np.float32)

def applyTilt():
    global height, width, l1, l2, d, result
    filtro = tilt_filter()

    filtro_negativo = np.ones([height, width], dtype=np.float32) - filtro

    for i in range(depth):
        result[:,:,i] = cv2.multiply(filtro,image[:,:,i])
        result[:,:,i] += cv2.multiply(filtro_negativo,image_2[:,:,i])
    
    cv2.imshow("tilt", np.array(result,dtype=np.uint8))


#print
cv2.namedWindow('tilt', cv2.WINDOW_NORMAL)
cv2.resizeWindow('tilt', 900, 600)
cv2.imshow("tilt",np.array(image,dtype=np.uint8))

trackbarName = "Y " + str(height)
cv2.createTrackbar(trackbarName,"tilt",l1,height,sety)

trackbarName = "DELTA " + str(height)
cv2.createTrackbar(trackbarName,"tilt",l2,height,setdelta)

trackbarName = "D "
cv2.createTrackbar(trackbarName,"tilt",d , 100, setd)

cv2.waitKey(0)
cv2.destroyAllWindows()