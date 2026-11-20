import cv2

pikachu = cv2.imread("pikachu.png")
cv2.imshow("Orignal Image", pikachu)

pikachu2 = cv2.resize(pikachu, (500, 250))
cv2.imshow("Resized Image", pikachu2)

cv2.waitKey(0)
cv2.destroyAllWindows()