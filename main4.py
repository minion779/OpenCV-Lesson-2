import cv2
import numpy as np

pikachu = cv2.imread("pikachu.png")
kernel = np.ones((3,3), np.uint8)
print(kernel)

kernel1 = np.ones((5,5), np.uint8)
print(kernel)

output2 = cv2.erode(pikachu, kernel1)
output1 = cv2.erode(pikachu, kernel)
cv2.imshow("erod", output1)
cv2.imshow("erod2", output2)
cv2.imshow("pikachuuu", pikachu)


cv2.waitKey(0)
cv2.destroyAllWindows()