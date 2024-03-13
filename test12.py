import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_OBSENSOR)
if cap is None or not cap.isOpened():
    sys.exit("warning: unable to open the camera")
color = 0
depth = 0
depth8u = 0

    