import os
import cv2

img = cv2.imread('Module 3/dog.jpg')
print(img.shape)
# cv2.imshow('dog', img)
# cv2.waitKey(0)

#crop_image
cropped_img = img[40:110, 65:150]
print(cropped_img.shape)
cv2.imshow('c_dog', cropped_img)
cv2.waitKey(0)

