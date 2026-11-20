import cv2

pikachu = cv2.imread("pikachu.png")
cv2.imshow("piki", pikachu)

borderedImage = cv2.copyMakeBorder(pikachu, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = 1)
cv2.imshow("pikiBorder", borderedImage)


cv2.waitKey(0)
cv2.destroyAllWindows()