import cv2

img = cv2.imread('Module_8 Drawing/whiteboard.png')
print(img.shape)

#line
cv2.line(img, (100, 150), (200, 400), (0, 255, 0), 3)

#rectangle
cv2.rectangle(img, (10, 250), (50, 350), (255, 0, 0), -1)

#circle
cv2.circle(img, (550, 550), 15, (0,0,255), -1)

#text
cv2.putText(img, 'Hey Guys!', (600, 450), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255, 200), 4)

cv2.imshow('board', img)
cv2.waitKey(0)