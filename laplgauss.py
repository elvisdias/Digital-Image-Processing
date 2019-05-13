import cv2
import numpy as np

def menu():
  print("\Press the key correspondent to the filter: \n"
        "a - abs\n"
        "m - mean\n"
        "g - gauss\n"
        "v - vertical\n"
        "h - horizontal\n"
        "l - laplacian\n"
        "p - gaussian laplacian\n"
        "esc - quit\n")  

def main():
    #definindo as matrizes de filtro 
    mean = np.array([[1,1,1],
                      [1,1,1],
                      [1,1,1]], dtype=np.float32)

    gauss = np.array([[1,2,1],
                     [2,4,2],
                     [1,2,1]], dtype=np.float32)

    horizontal = np.array([[-1,0,1],
                           [-2,0,2],
                           [-1,0,1]], dtype=np.float32)

    vertical = np.array([[-1,-2,-1],
                         [0,0,0],
                         [1,2,1]], dtype=np.float32)

    laplacian = np.array([[0,-1,0],
                         [-1,4,-1],
                         [0,-1,0]], dtype=np.float32)

    # camera = cv2.VideoCapture(0)

    #procedimento padrão para construção da matriz utilizada como máscara
    mask = mean
    mask1 = cv2.scaleAdd(mask, 1/9.0, np.zeros([3,3], dtype=np.float32))
    mask, mask1 = mask1, mask

    menu()

    absolut = True
    gray_image = cv2.imread("lenna.png", 0)
    imageFloat32 = np.array(gray_image, dtype=np.float32)
        
    while True:
        # return_value, image = camera.read()
        # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # imageFloat32 = np.array(gray_image, dtype=np.float32)
        frameFiltered = cv2.filter2D(imageFloat32, -1, mask, anchor=(1,1))
       
        if absolut:
            frameFiltered = abs(frameFiltered)
        
        result = np.array(frameFiltered, dtype=np.uint8)
        cv2.imwrite( "lenna.jpg", result)

        cv2.imshow("Filtering", result)

        key = cv2.waitKey(0) & 0xFF
        
        if key == 27:
            break
        elif key == ord('a'):
            absolut = not absolut
        elif key == ord('m'):
            mask = mean
            mask1 = cv2.scaleAdd(mask, 1/9.0, np.zeros([3,3], dtype = np.float32))
            mask = mask1
        elif key == ord('g'):
            mask = gauss
            mask1 = cv2.scaleAdd(mask, 1/16.0, np.zeros([3, 3], dtype = np.float32))
            mask = mask1
        elif key == ord('h'):
            mask = horizontal
        elif key == ord('v'):
            mask = vertical
        elif key == ord('l'):
            mask = laplacian
        elif key == ord('p'):            
            mask = gauss
            mask = cv2.scaleAdd(mask, 1/16.0, np.zeros([3, 3], dtype = np.float32))
            imageFloat32 = np.array(gray_image, dtype=np.float32)
            imageFloat32 = cv2.filter2D(imageFloat32, -1, mask, anchor = (1, 1))
            
            mask = laplacian
        else:
            pass
        # camera.release()
        cv2.destroyAllWindows()      
       

if __name__ == '__main__':
    main()