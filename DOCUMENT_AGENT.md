# Documentation Agent Instructions for Alien Invasion

You are an expert Python developer, technical writer, and AI documentation assistant.

Your task is to analyze this entire repository and generate complete and professional documentation.

## 1. Generate a README.md

The README must include:

### Project Title
A clear, professional title for the project:
e.g., “Alien Invasion — Python Pygame Game”.

### Description
Describe what this project does:
- A simple arcade-style game where the player controls a ship and shoots aliens.
- Mention that this project was built while following the book *Python Crash Course (3rd Edition)* as a learning project.

### Learning Source
Include a section named **“Learning Source / Inspiration”** with a professional note like:

> “This project was developed as part of learning Python by following the exercises and guidance in the book *Python Crash Course (3rd Edition)*.”  

### Features
Bullet list of key gameplay features (ship movement, firing bullets, alien movement, scoring).

### Project Structure
List and explain the main folders and Python files, e.g.:
- `alien_invasion.py` — entry point
- `settings/` — game configuration variables
- `ship/`, `enemy/`, `bullets/`, etc — components
- `highscore.txt` — stores persistent high score

### Setup & Installation
Include concise steps:
- Python version required
- How to install dependencies (if any like `pygame`)
- How to run the game

### ▶️ How To Play
Give instructions on controls (arrow keys, spacebar, etc.)

### 🧪 Notes / Troubleshooting
Optional section with common issues and tips.

### 📜 License
Add information about open source / usage rights if any.

## 2. Add Code Comments

For all Python modules:
- Insert clear comments above functions, classes, and complex logic.
- Explain how game loop, event handling, drawing, and updates work.

## 3. Add Internal Documentation Files (Optional)

If helpful, create folder documentation like:
- docs/STRUCTURE.md (explaining components)
- docs/CONTROLS.md (explaining controls and gameplay)

## 4. Quality Rules

- Do NOT change the core logic of game code.
- Keep comments concise and beginner-friendly.
- Avoid overly verbose text.
- Ensure README looks professional and easy to read.

## 5. Output Procedure

1. First generate a complete and polished **README.md**.
2. Then generate suggestions for file-level documentation and code comments.
