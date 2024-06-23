import cv2
import numpy as np

# Load the image
img = cv2.imread('Module_11 Feature Detection/bear.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting corners using the Harris corner detector
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Dilate the corner points to enhance the corner points
dst = cv2.dilate(dst, None)

# Thresholding to mark the corners
img[dst > 0.01 * dst.max()] = [0, 0, 255]

# Display the result
cv2.imshow('Harris Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
