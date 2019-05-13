import cv2

def main():
    image = cv2.imread("lenna.png", 0)

    for i in range(200,210):
        for j in range(10,200):
            image[i][j] = 0

    cv2.imshow("janela", image)
    cv2.imwrite( "lennaPixelsPreto.jpg", image)
    
    cv2.waitKey(0)
    
    image = cv2.imread("lenna.png", 1)
    
    for i in range (200,210):
        for j in range(10,200):
            image[i, j] = [0, 0, 255]
    
    cv2.imshow("janela", image)
    cv2.imwrite( "lennaPixelsVermelhos.jpg", image)

    cv2.waitKey(0) 
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    