import os
import cv2

#read_image
image_path = 'Module 2/Input/dog_image.jpeg'
img = cv2.imread(image_path)

#write_image
cv2.imwrite('Module 2/Input/dog_image_out.jpeg', img)

#visualize_image
cv2.imshow('Dog', img)
cv2.waitKey(5000) #if not given closed very fastly
