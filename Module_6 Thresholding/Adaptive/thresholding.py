import os
import cv2

img = cv2.imread('Module_6 Thresholding/Adaptive/handwritten.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, glob_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY )
ad_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

cv2.imshow('org', img)
cv2.imshow('gray', img_gray)
cv2.imshow('glob', glob_thresh)
cv2.imshow('thresh', ad_thresh)
cv2.waitKey(0)