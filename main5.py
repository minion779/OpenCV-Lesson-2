import cv2

pikachu = cv2.imread("pikachu.png")
cv2.imshow("pik", pikachu)

Gaussian = cv2.GaussianBlur(pikachu, (7,7), 0)
cv2.imshow("Gaussian Blurring", Gaussian)

median = cv2.medianBlur(pikachu, 5)
cv2.imshow("Median Blurring", median)

bilateral = cv2.bilateralFilter(pikachu, 9, 75, 75)
cv2.imshow("Bilateral Blurring", bilateral)


cv2.waitKey(0)
cv2.destroyAllWindows()