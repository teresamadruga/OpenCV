# https://docs.opencv.org/3.4/dd/d43/tutorial_py_video_display.html

import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    frame_is_read, frame = capture.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    cv2.imshow("frame", gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
