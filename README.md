# Rock-Paper-Scissors - Hand Tracker Game

A **rock-paper-scissors game** powered by OpenCV, utilizing **hand gesture recognition** to detect and interpret your hand movements.  
This interactive game lets you play against the computer, which randomly selects its moves. The system employs **real-time hand tracking** for a smooth and immersive experience.

## Features
- **Hand Gesture Recognition:** Detects your gestures (rock, paper, scissors) in real-time using MediaPipe's Hand Tracking.
- **Dynamic Countdown:** Displays a visual countdown ("Listo?", "Piedra", "Papel", "Tijera", "¡YA!") before each round.
- **Game Results:** Highlights the winner of each round for 3 seconds.
- **Interactive Design:** Enhanced aesthetics with smooth fonts and shadows.
- **User-Friendly:** Easy-to-use interface with clear instructions.

## How It Works
1. Place your hand in front of the camera.
2. Press the **spacebar** to start the game.
3. Follow the countdown and make your gesture when "¡YA!" appears.
4. The system detects your move and compares it to the computer's random selection.
5. The result is displayed on the screen: "Ganaste", "Perdiste", or "Empate".
6. Press "q" to exit the game.

## Technologies Used
- **Python:** Core programming language.
- **OpenCV:** For video capture and image processing.
- **MediaPipe:** For hand tracking and gesture recognition.
- **Numpy:** For efficient array manipulation.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/gaelgrcb/HandTracker-RockPaperScissors.git
    cd HandTracker-RockPaperScissors
    ```
2. Install the required dependencies:
    ```bash
    pip install opencv-python mediapipe numpy
    ```
3. Run the game:
    ```bash
    python Rock-Paper-Scissors.py
    ```

## Requirements
- Python 3.7 or higher
- Webcam or laptop camera
- Installed dependencies (OpenCV, MediaPipe, Numpy)

## Upcoming Improvements...
- **Multi-language support:** The game is currently designed in Spanish to cater to Spanish-speaking users. In future versions, we will add support for English and other languages.
- **Score Tracker:** A system will be implemented to track scores across multiple rounds of play.
- **Improved gesture detection:** Gesture detection will be enhanced to support a greater variety of hand angles.
