'''
Types :
- Sobel Derivatives
- Laplace Operator
- Canny Edge Detector

'''


import cv2
import numpy as np

img = cv2.imread('Module_7 Edge Detection/player.jpeg')

img_edge = cv2.Canny(img, 150, 300)

img_edge_d = cv2.dilate(img_edge, np.ones((2, 2), dtype = np.int8))
img_edge_e = cv2.erode(img_edge_d, np.ones((2, 2), dtype = np.int8))

cv2.imshow('player', img)
cv2.imshow('edge_player', img_edge)
cv2.imshow('edge_d_player', img_edge_d)
cv2.imshow('edge_e_player', img_edge_e)

cv2.waitKey(0)

