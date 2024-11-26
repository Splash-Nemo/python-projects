import pyaudio
import time
import cv2
import numpy
import pyautogui
from win32api import GetSystemMetrics

width= GetSystemMetrics(0)
height= GetSystemMetrics(1)

dim= (width, height)

f= cv2.VideoWriter_fourcc(*"XVID")

output= cv2.VideoWriter("screen-recorder/recodring.mp4", f, 30.0, dim)

start_time= time.time()
duration= 60+4
end_time= start_time + duration

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    img= pyautogui.screenshot()
    frame_1= numpy.array(img)
    frame= cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    current= time.time()
    cv2.imshow('Live', frame)
    if (current > end_time) or (cv2.waitKey(1) == ord('q')):
        break

output.release()
cv2.destroyAllWindows()