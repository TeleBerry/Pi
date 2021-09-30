from picamera import PiCamera
from time import sleep
import time
camera=PiCamera()
camera.rotation = 180

camera.start_preview(alpha=200)
i=4
while 8==8:
	now=time.strftime("%Y%m%d-%H%M%S")
	i=i+1
	sleep(2)
	camera.capture('/home/pi/image/%s.jpg'%now)
camera.stop_preview()

