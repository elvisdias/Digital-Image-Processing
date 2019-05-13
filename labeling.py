import cv2

def main():
    image = cv2.imread("bolhas.png",0)
    height, width = image.shape
    cv2.imshow("image", image)
    cv2.waitKey(0)

    #agora faz a contagem de fato
    nelem = 0
    for x in range(height):
        for y in range(width):
            if image[x,y] == 255:
                nelem += 1
                cv2.floodFill(image, None, (y,x), nelem)
                
    print("Number of elements: ", nelem)

    cv2.imshow("image", image)
    cv2.imwrite( "floodFill.jpg", image)
    cv2.waitKey(0)

    #torna elementos das bordas pretos percorrendo ambos lados de x e y
    for x in range(height):
        if image[x, 0] != 0:
            cv2.floodFill(image, None, (0, x),0)
        if image[x, width-1] != 0:
            cv2.floodFill(image, None, (width-1, x),0)

    for y in range(width):
        if image[0, y] != 0:
            cv2.floodFill(image, None, (y,0),0)
        if image[height-1, y] != 0:
            cv2.floodFill(image, None, (y, height-1), 0)
    
    cv2.imshow("image", image)
    cv2.imwrite( "apagarBordas.jpg", image)
    cv2.waitKey(0)

    cv2.floodFill(image, None, (0,0), 255)

    cont2 = 0

    for x in range(height):
        for y in range(width):
            if image[x, y] == 0:
                cv2.floodFill(image, None, (y,x), 255)
                cont2 += 1

    print("Number of holes: ", cont2)

    cv2.imshow("image", image)
    cv2.imwrite( "buraco.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main()
