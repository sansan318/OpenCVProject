
from email.mime import image
import cv2

print(cv2.getVersionString())

image = cv2.imread("lajiao1.png")
print(image.shape)


cv2.imshow("image",image)
cv2.waitKey()