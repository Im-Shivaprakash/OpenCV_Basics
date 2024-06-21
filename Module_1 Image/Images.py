import cv2
image = cv2.imread('Module 1/dog_image.jpeg')

#numpy array
print(type(image))

#shape of the image - (h,w,c)
print(image.shape)

'''

Image is made up of pixels
- most case value of pixel : 0 to 255
- binary case : [0,1] or [0,255]
- 16 bits image : 0 to 65535  #very rare

'''