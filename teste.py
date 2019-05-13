import cv2
import numpy as np
from math import exp, sqrt
gh, gl, c, d0 = 0, 0, 0, 0
g, cv, dv = 0,0,0

def aplicaFiltro():
    global gh, gl, c, d0, complex
    du = np.zeros(complex.shape, dtype=np.float32)
    for u in range(dft_M):
        for v in range(dft_N):
            du[u,v] = sqrt((u-dft_M/2.0)*(u-dft_M/2.0)+(v-dft_N/2.0)*(v-dft_N/2.0))

    du2 = cv2.multiply(du,du) / (d0*d0)
    re = np.exp(- c * du2)
    H = (gh - gl) * (1 - re) + gl
    #cv2.normalize(H, H, 0, 1, cv2.NORM_MINMAX)
    #cv2.imshow("mask", H[:,:,0])

    filtered = cv2.mulSpectrums(complex,H,0)
    #filtered = complex*H

    filtered = np.fft.ifftshift(filtered)
    filtered = cv2.idft(filtered)
    filtered = cv2.magnitude(filtered[:,:,0], filtered[:,:,1])
    #filtered, _ = cv2.split(filtered)

    cv2.normalize(filtered,filtered,0, 1, cv2.NORM_MINMAX)
    filtered = np.exp(filtered)
    cv2.normalize(filtered, filtered,0, 1, cv2.NORM_MINMAX)

    cv2.imshow("homomorfico", filtered)

def setgl(g):
    global gl
    gl = g/10.0
    if gl > gh:
        gl = gh-1
        gl = g / 10.0
    aplicaFiltro()

def setgh(g):
    global gh
    gh = g/10.0
    if 1 > gh:
        gh = 1
        gh = g / 10.0
    if gl > gh:
        gh = gl + 1
        gh = g / 10.0
    aplicaFiltro()

def setc(cv):
    global c
    if cv == 0:
        cv = 1
    c = cv/1000.0
    aplicaFiltro()

def setd0(dv):
    global d0
    d0 = dv/10.0
    if d0 == 0:
        d0 = 1
        d0 = dv / 10.0
    aplicaFiltro()


image = cv2.imread("lenna.png", 0)
cv2.imshow("original", image)
image = np.float32(image)
height, width = image.shape

dft_M = cv2.getOptimalDFTSize(height)
dft_N = cv2.getOptimalDFTSize(width)
padded = cv2.copyMakeBorder(image, 0, dft_M-height,0,dft_N-width, cv2.BORDER_CONSTANT, 0) + 1
padded = np.log(padded)
complex = cv2.dft(padded,flags=cv2.DFT_COMPLEX_OUTPUT)
complex = np.fft.fftshift(complex)
img_back = 20*np.log(cv2.magnitude(complex[:,:,0],complex[:,:,1]))
cv2.imshow("fft", np.uint8(img_back))
cv2.imshow("homomorfico", image)

trackbarName = "GL "
cv2.createTrackbar(trackbarName,"homomorfico",g,100,setgl)
trackbarName = "GH "
cv2.createTrackbar(trackbarName,"homomorfico",g,100,setgh)
trackbarName = "C "
cv2.createTrackbar(trackbarName,"homomorfico",cv,100,setc)
trackbarName = "D0 "
cv2.createTrackbar(trackbarName,"homomorfico",dv,dft_M,setd0)


cv2.waitKey(0)     
cv2.destroyAllWindows()