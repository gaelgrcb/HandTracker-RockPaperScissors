import cv2
import mediapipe as mp
import numpy as np

#Video Capture
camera = cv2.VideoCapture(0)

#Init MP and CV
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

#hands = mpHands.Hands(static_image_mode= False,
#                        min_detection_confidence= 0.9,
#                        min_tracking_confidence= 0.8)

#Function to detect hand gestures
def gestures(hand_landmarks):
    #We define the landmark of index and middle finger
    index_tip = hand_landmarks.landmark[8]
    middle_tip = hand_landmarks.landmark[12]

while True:
    success,img = camera.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    imgRGB = np.array(imgRGB, dtype=np.uint8)

    result = hands.process(imgRGB)

    if result.multi_hand_landmarks:
        for handLm in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLm, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Hand Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()