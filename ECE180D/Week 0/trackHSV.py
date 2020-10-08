#https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces
#https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html#contour-features

import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while(cap.isOpened()):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_color = np.array([30,100,100])
	upper_color = np.array([90,255,255])

	mask = cv2.inRange(hsv, lower_color, upper_color)

	contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	if len(contours) > 0:
		my_color_area = max(contours, key=cv2.contourArea)
		rect = cv2.minAreaRect(my_color_area)
		box = cv2.boxPoints(rect)
		box = np.int0(box)
		cv2.drawContours(frame,[box],0,(0,0,255),2)

	# Display the resulting frame
	cv2.imshow('frame',frame)
	k = cv2.waitKey(60) & 0xff
	if k == 27:
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()