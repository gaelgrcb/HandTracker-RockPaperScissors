<!DOCTYPE html>
<html>
<head>
    <title>Rock-Paper-Scissors Hand Tracker</title>
</head>
<body>
    <h1>Rock-Paper-Scissors Hand Tracker</h1>
    <p>
        A <strong>rock-paper-scissors game</strong> powered by OpenCV, utilizing <strong>hand gesture recognition</strong> to detect and interpret your hand movements. 
        This interactive game lets you play against the computer, which randomly selects its moves. The system employs <strong>real-time hand tracking</strong> for a smooth and immersive experience.
    </p>

    <h2>Features</h2>
    <ul>
        <li><strong>Hand Gesture Recognition:</strong> Detects your gestures (rock, paper, scissors) in real-time using MediaPipe's Hand Tracking.</li>
        <li><strong>Dynamic Countdown:</strong> Displays a visual countdown ("Listo?", "Piedra", "Papel", "Tijera", "¡YA!") before each round.</li>
        <li><strong>Game Results:</strong> Highlights the winner of each round for 3 seconds.</li>
        <li><strong>Interactive Design:</strong> Enhanced aesthetics with smooth fonts and shadows.</li>
        <li><strong>User-Friendly:</strong> Easy-to-use interface with clear instructions.</li>
    </ul>

    <h2>How It Works</h2>
    <ol>
        <li>Place your hand in front of the camera.</li>
        <li>Press the <strong>spacebar</strong> to start the game.</li>
        <li>Follow the countdown and make your gesture when "¡YA!" appears.</li>
        <li>The system detects your move and compares it to the computer's random selection.</li>
        <li>The result is displayed on the screen: "Ganaste", "Perdiste", or "Empate".</li>
        <li>Press "q" to exit the game.</li>
    </ol>

    <h2>Technologies Used</h2>
    <ul>
        <li><strong>Python:</strong> Core programming language.</li>
        <li><strong>OpenCV:</strong> For video capture and image processing.</li>
        <li><strong>MediaPipe:</strong> For hand tracking and gesture recognition.</li>
        <li><strong>Numpy:</strong> For efficient array manipulation.</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone this repository:
            <pre><code>git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio</code></pre>
        </li>
        <li>Install the required dependencies:
            <pre><code>pip install opencv-python mediapipe numpy</code></pre>
        </li>
        <li>Run the game:
            <pre><code>python game.py</code></pre>
        </li>
    </ol>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.7 or higher</li>
        <li>Webcam or laptop camera</li>
        <li>Installed dependencies (OpenCV, MediaPipe, Numpy)</li>
    </ul>

    <h2>File Structure</h2>
    <ul>
        <li><code>game.py</code>: Main game script.</li>
        <li><code>hand_tracker.py</code>: Standalone hand tracker module for demonstrations.</li>
        <li><code>README.md</code>: Documentation file.</li>
        <li><code>requirements.txt</code>: List of dependencies for quick setup.</li>
    </ul>

    <h2>Demo</h2>
    <p>Here’s a quick look at the game in action:</p>
    <p><em>(Insert a GIF or screenshots of the game)</em></p>

    <h2>Upcoming Improvements</h2>
    <ul>
      <li><strong>Multi-language support:</strong> The game is currently designed in Spanish to cater to Spanish-speaking users. In future versions, we will add support for English and other languages, allowing more people to enjoy the game.</li>
      <li><strong>Score Tracker:</strong> A system will be implemented to track scores across multiple rounds of play.</li>
      <li><strong>Improved gesture detection:</strong> Gesture detection will be enhanced to support a greater variety of hand angles.</li>
    </ul>

    <h2>Contributing</h2>
    <p>Feel free to fork this repository and submit a pull request with your improvements. Contributions are always welcome!</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <code>LICENSE</code> file for details.</p>

    <h2>Acknowledgments</h2>
    <ul>
        <li>MediaPipe for providing robust hand tracking.</li>
        <li>OpenCV for enabling real-time video capture and processing.</li>
    </ul>
</body>
</html>
