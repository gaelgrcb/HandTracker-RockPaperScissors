import time
import cv2
import mediapipe as mp
import numpy as np
import random

#Init MP and CV
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_drawing = mp.solutions.drawing_utils

#Function to draw texts
def draw_centered_text(frame, text, font, font_scale, thickness, color, shadow_color=None, y_offset=0):
    window_height, window_width, _ = frame.shape

    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    text_width, text_height = text_size

    x = (window_width - text_width) // 2
    y = (window_height + text_height) // 2 + y_offset

    if shadow_color:
        cv2.putText(frame, text, (x + 2, y + 2), font, font_scale, shadow_color, thickness + 2, lineType=cv2.LINE_AA)

    cv2.putText(frame, text, (x, y), font, font_scale, color, thickness, lineType=cv2.LINE_AA)

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

#Texts to start the round
countdown_texts = ["Listo?","Piedra","Papel","Tijera","YA"]

#Game states
waiting_for_space = True
round_active= False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgRGB = np.array(imgRGB, dtype=np.uint8)
    result = hands.process(imgRGB)

    current_time = time.time()

    if waiting_for_space:
        draw_centered_text(
            frame,
            "Presiona SPACEBAR",
            font=cv2.FONT_HERSHEY_SIMPLEX,
            font_scale=1,
            thickness=2,
            color=(0, 255, 255),
            shadow_color=(0, 0, 0),
            y_offset=0
        )

        if cv2.waitKey(1) & 0xFF == ord(' '):
            waiting_for_space = False
            round_active = True
            last_game_time = current_time
    elif round_active:
        elapsed_time = current_time - last_game_time
        if elapsed_time <= 5:
            if elapsed_time < 4:
                countdown_index = int(elapsed_time)
                countdown_message = countdown_texts[countdown_index]
            else:
                countdown_message = countdown_texts[-1]

            draw_centered_text(
                frame,
                countdown_message,
                font=cv2.FONT_HERSHEY_SIMPLEX,
                font_scale=2,
                thickness=4,
                color=(0, 255, 255),
                shadow_color=(0, 0, 0),
                y_offset=0
            )
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
            draw_centered_text(frame, f"Jugador: {my_move if my_move else 'NO JUGO'}", cv2.FONT_HERSHEY_SIMPLEX, 1, 2, (0, 255, 0), (0, 0, 0), -100)
            draw_centered_text(frame, f"Computadora: {computer_move}", cv2.FONT_HERSHEY_SIMPLEX, 1, 2, (0, 0, 255), (0, 0, 0), -50)
            draw_centered_text(frame, f"Resultado: {game_result}", cv2.FONT_HERSHEY_SIMPLEX, 1, 2, (255, 255, 0), (0, 0, 0), 0)
        else:
            my_move = ""
            computer_move = ""
            game_result = ""
            waiting_for_space = True
            round_active = False

    cv2.imshow("Piedra, Papel o Tijera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()