import cv2

TOP_SLIDER = 10
TOP_SLIDER_MAX = 200
t1 = 10
T1 = 10
edges = 0

def setT1(t1):
    global T1
    T1 = t1
    print(t1)
    if T1 < TOP_SLIDER:
        T1 = 10
    edges = cv2.Canny(image, T1, 3*T1) 
    cv2.imshow("canny", edges)

image = cv2.imread('lenna.png', 0)
edges = cv2.Canny(image, T1, 3*T1) 
cv2.imshow("canny", edges)
cv2.createTrackbar("T1", "canny", t1, TOP_SLIDER_MAX, setT1)

cv2.waitKey(0)     
cv2.destroyAllWindows()
