import os 
import cv2

img = cv2.imread('Module 3/dog.jpg')
print(img.shape)

#resize-img
resize_img = cv2.resize(img, (100,100))
print(resize_img.shape)


cv2.imshow('dog', img)
cv2.imshow('r_dog', resize_img)
cv2.waitKey(0)
