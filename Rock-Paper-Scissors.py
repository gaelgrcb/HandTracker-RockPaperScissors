import cv2
import mediapipe as mp
import numpy as np

camera = cv2.VideoCapture(0)
mpHands = mp.solutions.hands

hands = mpHands.Hands(satic_image_mode = False,
                        min_detection_confidence= 0.9,
                        min_tracking_confidence= 0.8)
mpDraw = mp.solutions.drawing_utils

while True:
    success,img = camera.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)