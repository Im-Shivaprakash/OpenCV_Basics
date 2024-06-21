import os
import cv2

#read_video
video_path = os.path.join('.', 'Module 2', 'Video', 'Test_video1.mp4')
video = cv2.VideoCapture(video_path)

#visualize_video
ret = True
while ret:
    ret, frame = video.read() #ret is a boolean value defining whether new frame is there or not
    
    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(30)

video.release()
cv2.destroyAllWindows()