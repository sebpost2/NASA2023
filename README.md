# Titan3023 - NASA Hackathon 2023

### Project Overview
**Titan3023** is a kid-friendly educational game developed for the NASA Hackathon 2023. The goal was to create an interactive game that introduces children to space exploration—specifically, the fascinating moons of Saturn. In the game, players control an astronaut navigating between Saturn’s moons, each with its own set of challenges (such as unstable weather and harsh conditions). While onboard the spacecraft, a virtual captain (intended to use the OpenAI API for answering space-related questions) provides educational insights and fun facts about space. Although the OpenAI API integration was planned, it was not implemented during the hackathon.

---

### Key Features
- **Interactive Gameplay:**  
  - Control an astronaut using keyboard inputs.
  - Visit various Saturn moons, each presenting different difficulty levels.
  - Unique environmental challenges simulate unstable weather and extreme conditions.

- **Educational Content:**  
  - Intended integration of an AI-driven captain to answer kids’ questions about space, fostering curiosity and learning.
  - Engaging visuals and animations to introduce basic concepts of space exploration.

- **Dynamic Animations & Controls:**  
  - Sprite sheet animations for the astronaut and environmental effects (e.g., tornado animations).
  - Randomized mini-game mechanics that require players to press specific keys in sequence.

- **Modular Design:**  
  - Organized code with separate classes for animations, button controls, and game logic.
  - Designed using Python and Pygame for rapid prototyping and engaging gameplay.

---

### Technologies Used
- **Python & Pygame:** For game development, handling graphics, animations, and user input.
- **Queue Module:** To manage the sequence of key inputs during mini-games.
- **Random Module:** To add variability in challenges and key sequences.
- **Sprite Sheet Handling:** Custom classes to divide and animate sprite sheets.

---

### How to Run the Game
1. **Prerequisites:**  
   - Python 3.x installed  
   - Pygame library installed (you can install it via `pip install pygame`)

2. **Setup:**  
   - Clone the repository and navigate to the project folder.
   - Ensure that the `assets` folder (containing sprites, background images, and buttons) is in the correct directory relative to the main script.

3. **Run the Game:**  
   ```bash
   python3 OpenGLCode.py
   ```
   > Note: In this project, the main file is named `OpenGLCode.cpp` in previous projects, but for the NASA project, the game code is written in Python. Replace `OpenGLCode.py` with the appropriate filename if different.

---

### Gameplay Instructions
- **Main Menu:**  
  - Start the game by clicking the "Start" button on the main menu.
  
- **During Gameplay:**  
  - Control the astronaut with keyboard inputs (`W`, `A`, `S`, `D`) as prompted by on-screen cues.
  - Avoid collisions with obstacles (like tornado animations) and navigate your spaceship safely through Saturn’s challenging moons.
  - The game dynamically adjusts difficulty based on the environmental conditions of each moon.

- **Educational Component:**  
  - Although the captain’s interactive Q&A via OpenAI API was planned, the current version does not include this feature.
  - Future iterations may integrate AI responses to provide real-time educational content.

---

### Future Enhancements
- **OpenAI API Integration:**  
  - Implement the API to enable the captain to answer space-related questions, adding an interactive educational layer.
- **Expanded Levels & Content:**  
  - Introduce more moons with varying challenges.
  - Enhance environmental effects and background details.
- **Improved User Interface:**  
  - Refine the main menu and in-game UI for a smoother experience.
- **Additional Educational Modules:**  
  - Incorporate mini-lessons or fun facts during level transitions.
