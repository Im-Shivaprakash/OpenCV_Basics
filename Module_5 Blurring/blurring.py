'''

- The use of blurring is to reduce noise in the image.
- It is one of the basic denoising method
- Intuition : Averages all the neighbourhood pixels 
- Types:
    - blur()
    - GaussianBlur()
    - medianBlur()
    - bilateralFilter()

'''

import os
import cv2
img = cv2.imread('Module_5 Blurring/bird.jpeg')

# blurring
k_size = 5
blur_image = cv2.blur(img, (k_size,k_size))
gau_image = cv2.GaussianBlur(img, (k_size,k_size), 3)
med_image = cv2.medianBlur(img,k_size)

cv2.imshow('bird', img)
cv2.imshow('blur_bird', blur_image)
cv2.imshow('gau_bird', gau_image)
cv2.imshow('med_bird', med_image)
cv2.waitKey(0)

# removing_noise
img = cv2.imread('Module_5 Blurring/cow.png')
k_size = 5
blur_image = cv2.blur(img, (k_size,k_size))
gau_image = cv2.GaussianBlur(img, (k_size,k_size), 3)
med_image = cv2.medianBlur(img,k_size)

cv2.imshow('cow', img)
cv2.imshow('blur_cow', blur_image)
cv2.imshow('gau_cow', gau_image)
cv2.imshow('med_cow', med_image)
cv2.waitKey(0)
