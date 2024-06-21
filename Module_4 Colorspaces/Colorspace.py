import os
import cv2

img_path = 'Module_4 Colorspaces/bird.jpeg'
img = cv2.imread(img_path)
cv2.imshow('bird', img)
# cv2.waitKey(0)

# default colorspace is bgr

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


cv2.imshow('rgb-bird', img_rgb)
cv2.imshow('gray-bird', img_gray)
cv2.imshow('hsv-bird', img_hsv)
cv2.waitKey(0)