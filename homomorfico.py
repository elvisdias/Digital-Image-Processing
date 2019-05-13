import cv2
import numpy as np
from math import exp, sqrt

#http://photoandtravels.blogspot.com/2011/04/against-light-photography.html
image = cv2.imread("teste.jpg", 0)
height, width = image.shape
dft_M = cv2.getOptimalDFTSize(height)
dft_N = cv2.getOptimalDFTSize(width)

#Inicialização de parâmetros globais da formula
yh, yl, c, d0, = 0, 0, 0, 0
#Inicialização de parâmetros globais setados pelo usuáro
y_track, d0_track, c_track = 0, 0, 0
complex = 0 

def homomorphic():
    global yh, yl, c, d0, complex
    du = np.zeros(complex.shape, dtype = np.float32)
    #H(u, v)
    for u in range(dft_M):
        for v in range(dft_N):
            du[u,v] = sqrt((u - dft_M/2.0)*(u - dft_M/2.0) + (v - dft_N/2.0)*(v - dft_N/2.0))

    du2 = cv2.multiply(du,du) / (d0*d0)
    re = np.exp(- c * du2)
    H = (yh - yl) * (1 - re) + yl
    #S(u, v)
    filtered = cv2.mulSpectrums(complex, H, 0)
     #inverse DFT (does the shift back first)
    filtered = np.fft.ifftshift(filtered)
    filtered = cv2.idft(filtered)
    #normalization to be representable 
    filtered = cv2.magnitude(filtered[:, :, 0], filtered[:, :, 1])
    cv2.normalize(filtered, filtered, 0, 1, cv2.NORM_MINMAX)
    #g(x, y) = exp(s(x, y))
    filtered = np.exp(filtered)
    cv2.normalize(filtered, filtered,0, 1, cv2.NORM_MINMAX)
    
    cv2.namedWindow('homomorphic', cv2.WINDOW_NORMAL)
    cv2.imshow("homomorphic", filtered)
    cv2.resizeWindow("homomorphic", 600, 550)
    
def setyl(y_track):
    global yl
    yl = y_track
    if yl == 0:
        yl = 1
    if yl > yh:
        yl = yh - 1
    homomorphic()

def setyh(y_track):
    global yh
    yh = y_track
    if yh == 0:
        yh = 1
    if yl > yh:
        yh = yl + 1
    homomorphic()

def setc(c_track):
    global c
    c = c_track/1000.0
    if c == 0:
        c_track = 1    
    homomorphic()

def setd0(d0_track):
    global d0
    d0 = d0_track
    if d0 == 0:
        d0 = 1
    homomorphic()

def main():
    # copyMakeBorder(src, top, bottom, left, right, borderType[, dst[, value]]) 
    # BORDER_CONSTANT = Pad the image with a constant value (i.e. black or 0)
    padded = cv2.copyMakeBorder(image, 0, dft_M - height, 0, dft_N - width, cv2.BORDER_CONSTANT, 0) 
    # +1 pra tratar log(0)
    padded = np.log(padded+1)
    global complex
    complex = cv2.dft(np.float32(padded)/255.0, flags = cv2.DFT_COMPLEX_OUTPUT)
    complex = np.fft.fftshift(complex)
    img = 20 * np.log(cv2.magnitude(complex[:,:,0], complex[:,:,1]))
    
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", image)
    cv2.imwrite( "teste2.jpg", image)
    cv2.resizeWindow("Image", 400, 400)

    cv2.namedWindow('DFT', cv2.WINDOW_NORMAL)
    cv2.imshow("DFT", np.uint8(img))
    cv2.imwrite( "dft.jpg", np.uint8(img))
    cv2.resizeWindow("DFT", 250, 250)

    cv2.createTrackbar("YL", "Image", y_track, 100, setyl)
    cv2.createTrackbar("YH", "Image", y_track, 100, setyh)
    cv2.createTrackbar("C", "Image", c_track, 100, setc)
    cv2.createTrackbar("D0", "Image", d0_track, 100, setd0)
 
    cv2.waitKey(0)     
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()