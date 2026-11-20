import cv2

ash = cv2.imread("ash.png")
pikachu = cv2.imread("pikachu.png")

output = cv2.subtract(ash, pikachu)

cv2.imshow("bothh", output)


cv2.waitKey(0)
cv2.destroyAllWindows()