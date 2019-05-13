import cv2
from  matplotlib import pyplot as plt 

# camera = cv2.VideoCapture(0)
nbins = 256
#while True:
#return_value, image = camera.read()
#if 1:
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.imread("lenna.png", 0)
cv2.imshow("Normal", image)
cv2.imwrite( "lennaBW.jpg", image)
hist = cv2.calcHist([image], [0], None, [256], [0,256])

cv2.waitKey(0)

image = cv2.equalizeHist(image)

hist2 = cv2.calcHist([image], [0], None, [nbins], [0,256])
cv2.imshow("Equalized", image)
cv2.imwrite( "lennaEqualized.jpg", image)
cv2.waitKey(0)

plt.plot(hist, 'b')
plt.plot(hist2, 'r')
plt.xlim([0,nbins])
plt.show()

cv2.waitKey(0)     
#camera.release()
cv2.destroyAllWindows()
#else: 
    #   camera.release()
    #  break

