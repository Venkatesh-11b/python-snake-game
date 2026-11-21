# Python Snake Game (Turtle Graphics)

An interactive Snake Game developed in Python using the built-in `turtle`, `time`, and `random` modules. Built as a mini project for *UGE3188 – Problem Solving and Programming using Python*.

## Features
- **WASD Controls:** Smooth 4-directional movement (`W`, `A`, `S`, `D`) with reverse-direction lock to prevent accidental self-collision.
- **Dynamic Difficulty:** Movement delay automatically decreases as your score crosses 50, 100, and 150 points.
- **Live Scoreboard:** Tracks current score (+10 per food) and session high score in real time.
- **Collision Detection:** Resets the snake and score upon hitting the screen borders or its own body segments.

## How to Run
Ensure Python 3 is installed on your system (no external `pip` packages required), then run:

```bash
python snake_game.py
