# 🐍Wormy - Pygame

A modern implementation and architectural refactoring of the classic Snake/Wormy game using **Python 3.10+** and **Pygame**. 

This project transforms standard game code into a clean, maintainable, and highly decoupled codebase by applying key **Software Engineering** principles.

---

## 🛠️ Key Architectural Highlights

* **Separation of Concerns (SoC):** 
  * `logic.py`: Game state, grid tracking, and collision logic independent of UI rendering.
  * `graphics.py`: Dedicated rendering layer using Pygame surfaces.
  * `move.py`: User input handling mapped clean to logical state updates.
  * `states.py`: Type-safe state management leveraging Python `Enum` and `auto()`.

* **Optimal Data Structures:**
  * Utilized `collections.deque` (FIFO queue) to model the snake body, ensuring $O(1)$ time complexity for constant-time head additions (`append`) and tail truncations (`popleft`).

* **Externalized Configuration:**
  * System parameters (window size, colors, speed difficulty) are loaded dynamically from `config_basic.json` into `constants.py` with assertion guards to eliminate hardcoding.

* **Modern Python Features:**
  * Clean control flow using Structural Pattern Matching (`match-case` statements).
  * Robust code clarity with explicit Type Hints throughout the classes.
  * Dynamic frame rate scaling based on user-selected difficulty levels (`EASY`, `MEDIUM`, `HARD`, `EXPERT`).

---

## 📁 Project Structure

```text
├── config_basic.json     # External configuration parameters
├── constants.py          # Loaded settings & assertion rules
├── states.py             # Enums for Game State, Levels, and Directions
├── logic.py              # Pure game logic & deque data structures
├── graphics.py           # Rendering & Pygame UI abstractions
├── move.py               # Keyboard event handler
├── game.py               # Main gameplay loop & pause handling
├── game_over.py          # Game Over UI overlay & navigation
├── menu.py               # Animated main menu system
├── terminate.py          # Clean exit routines
└── main.py               # Application entry point

## 🔗 Other Refactored Games: Check out in my profile 📓 simple-games-with-pygame 
