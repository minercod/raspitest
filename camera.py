import cv2
import time
from picamera import PiCamera
from picamera.array import PiRGBArray

cam = PiCamera()
cam.resolution = (600,480)
cam.hflip = False
cam.vflip = True
cam.rotation = 0
rawcam = PiRGBArray(cam, size=(600, 480))
time.sleep(0.1)
for frame in cam.capture_continuous(rawcam, format='bgr', use_video_port=True):
	image = frame.array
	cv2.imshow('Frame', image)
	key = cv2.waitKey(1) & 0xFF
	rawcam.truncate(0)
	if key == ord('q'):
		break

