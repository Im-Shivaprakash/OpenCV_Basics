import os
import cv2

img = cv2.imread('Module_6 Thresholding/Global/bear.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
final = cv2.medianBlur(thresh, 5)

cv2.imshow('bear', img)
cv2.imshow('bear_gry', img_gray)
cv2.imshow('bear_thrsh', thresh)
cv2.imshow('bear_final', final)


cv2.waitKey(0)