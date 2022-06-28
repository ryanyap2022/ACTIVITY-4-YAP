Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======== RESTART: C:/Users/FUJITSU/opencv_folder/ACTIVITY-4-YAP/cute.py ========
Traceback (most recent call last):
  File "C:/Users/FUJITSU/opencv_folder/ACTIVITY-4-YAP/cute.py", line 4, in <module>
    cv2.imshow('cutieeee', img)
cv2.error: OpenCV(4.6.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:967: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'


======== RESTART: C:/Users/FUJITSU/opencv_folder/ACTIVITY-4-YAP/cute.py ========
import cv2
file = 'cat.jpg'
img = cv2.imread(file, 1)
cv2.imshow('cutieeee', img)
cv2.waitKey(0)
cv2.destroyAllWindows