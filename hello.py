import cv2

while(1):
    image = cv2.imread("biel.png",0)
    cv2.namedWindow("image")
    cv2.imshow("image", image)

    key = cv2.waitKey(33)
    if key==27:    # Esc key to stop
        break
