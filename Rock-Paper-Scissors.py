import cv2
import mediapipe as mp
import numpy as np
import random

#Init MP and CV
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

#hands = mpHands.Hands(static_image_mode= False,
#                        min_detection_confidence= 0.9,
#                        min_tracking_confidence= 0.8)

#Function to detect hand gestures
def gestures(hand_landmarks):
    #We define the landmark of index and middle finger
    index_tip = hand_landmarks.landmark[8]
    middle_tip = hand_landmarks.landmark[12]

    #Calculate the distance between finger an middle finger
    distance = ((index_tip - middle_tip) ** 2 + (index_tip.y - middle_tip.y) ** 2) * 0.5

    if distance < 0.05:
        return "Tijera"
    elif index_tip < middle_tip.y:
        return "Papel"
    else:
        return "Piedra"

#Function to determinate the winner
def winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Empate"
    #Win combinations
    elif (player_choice == "Piedra" and computer_choice == "Tijera") or (player_choice == "Tijera" and computer_choice == "Papel") or (player_choice == "Papel" and computer_choice == "Piedra"):
        return "Ganaste"
    else:
        return "Perdiste"

#Video Capture
camera = cv2.VideoCapture(0)
while True:
    success,img = camera.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    imgRGB = np.array(imgRGB, dtype=np.uint8)

    result = hands.process(imgRGB)

    if result.multi_hand_landmarks:
        for handLm in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, handLm, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Tracker", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()