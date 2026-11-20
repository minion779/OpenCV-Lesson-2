import cv2

ash = cv2.imread("ash.png")
pikachu = cv2.imread("pikachu.png")

output = cv2.addWeighted(ash, 0.5, pikachu, 0.4, 0)
cv2.imshow("both", output)


cv2.waitKey(0)
cv2.destroyAllWindows()