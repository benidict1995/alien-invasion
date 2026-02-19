# 🟢 Alien Invasion — Python Pygame Game

## 📌 Description
Alien Invasion is a simple arcade-style game built with Python and Pygame. The player controls a ship that moves horizontally and shoots bullets to destroy waves of invading aliens. This repository contains the game source, assets, and minimal persistence for high scores.

Learning note: This project was developed as part of learning Python by following the exercises and guidance in the book *Python Crash Course (3rd Edition)*.

## 📘 Learning Source / Inspiration
> This project was developed as part of learning Python by following the exercises and guidance in the book *Python Crash Course (3rd Edition).*  

## ⚙️ Features
- Player ship movement (left / right)
- Fire bullets to destroy aliens
- Alien fleet movement and formation behavior
- Collision detection and scoring
- Levels and increasing difficulty
- Lives and game over handling
- Persistent high score stored in a simple text file

## 📂 Project Structure (high level)
- `alien_invasion.py` — entry point to start the game and main loop
- `settings/` or `settings.py` — game configuration variables (screen size, colors, speeds)
- `ship/` or `ship.py` — ship class and movement logic
- `enemy/` or `alien.py` — alien class and fleet behavior
- `bullets/` or `bullet.py` — bullet handling and collision checks
- `game_stats.py` — tracks scores, levels, and game state
- `scoreboard.py` — renders current score, high score, level, and lives
- `button.py` — play/menus UI components
- `resources/images/` — image assets for ship, aliens, bullets
- `resources/sounds/` — optional sound assets
- `highscore.txt` — simple persistent storage for the high score
- `docs/` — (optional) internal documentation and guides

Note: Exact module and folder names may vary; this README documents the intended organization and responsibilities of the main components.

## 🚀 Setup & Installation
1. Install Python 3.8+ (3.10 or newer recommended).
2. Create and activate a virtual environment (recommended):
   - python -m venv venv
   - source venv/bin/activate (macOS / Linux) or venv\Scripts\activate (Windows)
3. Install dependencies:
   - pip install pygame
4. Run the game:
   - python alien_invasion.py

If the project includes a requirements file:
- pip install -r requirements.txt

## ▶️ How To Play
- Move the ship: Left / Right arrow keys (or A / D).
- Fire bullets: Spacebar.
- Start / Pause: Press the Play button (if present) or the configured key (often "P").
- Quit: Q key or close the window.
- Objective: Destroy all aliens in a wave, avoid collisions, and achieve a high score.

Controls may vary slightly depending on the specific implementation in this repository. Check the game's startup or docs for any custom bindings.

## 🧪 Notes / Troubleshooting
- Pygame install issues:
  - On macOS, ensure you have a recent Python and Xcode command line tools installed.
  - On Linux, you may need SDL-related dev packages (e.g., libsdl2-dev).
- If the game window does not appear or closes immediately, run from a terminal to see error messages.
- Resource paths: If images or sounds fail to load, ensure relative paths are correct and that you run the game from the project root.
- High score persistence: `highscore.txt` must be writable; create the file if missing and give write permissions.

## 📜 License
This repository is provided under the MIT License. You are free to use, modify, and distribute the code with attribution. See the LICENSE file (if present) for full terms.

## Suggestions for repository documentation and code comments
- Add docs/STRUCTURE.md describing each module and data flow.
- Add docs/CONTROLS.md listing default controls and configurable keys.
- Add concise comments at the top of each module and above classes/functions:
  - Explain responsibilities (e.g., Ship handles input and movement).
  - Comment the game loop: event handling → update state → drawing.
  - Document collision handling and score updates.
- Keep comments beginner-friendly and avoid changing game logic.

Enjoy exploring and extending Alien Invasion!