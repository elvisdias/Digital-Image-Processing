import cv2 

camera = cv2.VideoCapture(0) #0 for webcam, 1 for second camera etc

#Chi-square distance is one of the distance measures that can be used as a measure of dissimilarity between two histograms
#maxima distancia adotada
maxDist = 200


while True:
    #return_value = 0 for some error or 1 for successful reading
    #image is the frame capturedx
    return_value, image = camera.read()
    if return_value:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("image",  gray_image)

        H1 = cv2.calcHist( gray_image, [0], None, [256], [0,256])
        H2 = cv2.calcHist(gray_image, [0], None, [256], [0,256])
        comp = cv2.compareHist(H1, H2, cv2.HISTCMP_CHISQR)
        
        height, width = gray_image.shape
        while comp >= maxDist:
            for x in range(height):
                gray_image[x,0] = 255
                gray_image[x, width-1] = 255
            
            for y in range(width):
                gray_image[0,y] = 255                    
                gray_image[height-1, y] = 255
            
            cv2.imshow("image",  gray_image)
            
            H1 = cv2.calcHist( gray_image, [0], None, [256], [0,256])
            H2 = cv2.calcHist(gray_image, [0], None, [256], [0,256])
            comp = cv2.compareHist(H1, H2, cv2.HISTCMP_CHISQR)
            print(comp)
                             
        cv2.waitKey(0)        
        camera.release()
        cv2.destroyAllWindows()
    else: 
        camera.release()
        break