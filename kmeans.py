#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html
import cv2
import numpy as np

def main():
    
    NCLUSTERS = 8
    NROUNDS = 1
    
    image = cv2.imread("praia.jpg", 1)
    height, width, channels = image.shape
    samples = np.zeros([height*width, 3], dtype = np.float32)
    count = 0
    
    for x in range(height):
        for y in range(width):
            samples[count] = image[x][y] #BGR color
            count += 1
            
    compactness, labels, centers = cv2.kmeans(samples,
                                        NCLUSTERS, 
                                        None,
                                        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001), 
                                        NROUNDS, 
                                        cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    image2 = res.reshape((image.shape))
    
    cv2.imshow("KMEANS", image2)
    cv2.imwrite("kmeans15.jpg", image2)
    cv2.waitKey(0)     
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()