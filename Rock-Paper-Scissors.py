import time
import cv2
import mediapipe as mp
import numpy as np
import random

#Init MP and CV
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_drawing = mp.solutions.drawing_utils

#Function to detect hand gestures
def gestures(hand_landmarks):
    fingers = []
    landmarks = hand_landmarks.landmark

    fingers.append(1 if landmarks[4].x < landmarks[3].x else 0)
    for i in [8, 12, 16, 20]:
        fingers.append(1 if landmarks[i].y < landmarks[i - 2].y else 0)

    if fingers == [0, 1, 1 ,0, 0]:
        return "Tijera"
    elif fingers == [1, 1, 1, 1, 1]:
        return "Papel"
    elif fingers == [0, 0, 0, 0, 0]:
        return "Piedra"
    return None

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

last_game_time = time.time()
last_result_time = None
game_result = ""
my_move = ""
computer_move = ""
round_active= True
countdown_texts = ["Listo?","Piedra","Papel","Tijera","YA"]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgRGB = np.array(imgRGB, dtype=np.uint8)
    result = hands.process(imgRGB)

    current_time = time.time()

    if round_active:
        elapsed_time = current_time - last_game_time
        if elapsed_time <= 4:
            if elapsed_time < 4:
                countdown_index = int(elapsed_time)
                countdown_message = countdown_texts[countdown_index]
            else:
                countdown_message = countdown_texts[-1]

            cv2.putText(frame, countdown_message, (200, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)
        else:
            if result.multi_hand_landmarks:
                for handLm in result.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, handLm, mp_hands.HAND_CONNECTIONS)
                    my_move = gestures(handLm)

            computer_move = random.choice(["Piedra", "Papel", "Tijera"])
            game_result = winner(my_move, computer_move)
            round_active = False
            last_result_time = current_time
    else:
        if current_time - last_result_time <= 3:
            cv2.putText(frame, f"Jugador: {my_move if my_move else 'Descalificado'}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Computadora: {computer_move}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(frame, f"Resultado: {game_result}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        else:
            my_move = ""
            computer_move = ""
            game_result = ""
            last_game_time = current_time
            round_active = True

    cv2.imshow("Piedra, Papel o Tijera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()