import cv2
import numpy as np

def main():
    image = cv2.imread("lenna.png", 0)

    height, width = image.shape
    #corta a imagem no meio de seu comprimento no sentido horizontal
    [h,w] = np.split(image, [int(height/2)], 0)
    #concatena na ordem contrária no sentido horizontal
    image = np.concatenate((w,h))
    # contra a imagem no meio de sua largura no sentido vertical 
    [h,w] = np.split(image,[int(width/2)], 1)
    #concatena na ordem contrária no sentido vertical
    image = np.concatenate((w,h),1)

    cv2.imshow("image",image)
    cv2.imwrite( "quadrantes.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
