# executar com python regions.py 100 200 30 150 por exemplo

import cv2, sys

def main():
    image = cv2.imread("lenna.png", 0)

    for i in range(int(sys.argv[1]),int(sys.argv[2])):
        for j in range(int(sys.argv[3]),int(sys.argv[4])):
            image[i][j] = 255 - image[i][j] 

    cv2.imshow("image", image)    
    cv2.imwrite( "negativo.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()


