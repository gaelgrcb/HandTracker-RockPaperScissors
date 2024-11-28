import cv2
import mediapipe as mp
import numpy as np
import random

#Init MP and CV
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
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
    distance = ((index_tip.x - middle_tip.x) ** 2 + (index_tip.y - middle_tip.y) ** 2) * 0.5

    if distance < 0.05:
        return "Tijera"
    elif index_tip.y < middle_tip.y:
        return "Papel"
    else:
        return "Piedra"

#Function to determinate the winner
def winner(player_move, computer_move):
    if player_move == computer_move:
        return "Empate"
    #Win combinations
    elif (player_move == "Piedra" and computer_move == "Tijera") or (player_move == "Tijera" and computer_move == "Papel") or (player_move == "Papel" and computer_move == "Piedra"):
        return "Ganaste"
    else:
        return "Perdiste"

#Video Capture "UPDATED"
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgRGB = np.array(imgRGB, dtype=np.uint8)
    result = hands.process(imgRGB)

    if result.multi_hand_landmarks:
        for landamark in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, landamark, mp_hands.HAND_CONNECTIONS)
            my_move = gestures(landamark)
            #Show my gesture in screen
            cv2.putText(frame, f"Jugador: {my_move}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

            #Computer random move
            computer_move = random.choice(["Piedra", "Papel", "Tijera"])
            cv2.putText(frame, f"Computadora: {computer_move}", (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)

            #compare moves
            result_text = winner(my_move, computer_move)
            cv2.putText(frame,f"Resultado: {result_text}", (10,110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)

    cv2.imshow("Piedra, Papel o Tijera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()