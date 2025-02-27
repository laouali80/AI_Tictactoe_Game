# AI Tic-Tac-Toe Game

A Tic-Tac-Toe game implemented with Artificial Intelligence (AI). The AI uses the Minimax algorithm to maximize its chances of winning or forcing a tie.

- **Minimax** and **Alpha-Beta Pruning** Algorithm:  
  Youtube: [https://www.youtube.com/watch?v=l-hh51ncgDI]

---

## Requirements

To run this project, ensure you have the following:

- **Python** version **3.12.2** or higher  
  Download Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## Getting Started

Follow these steps to set up and run the project:

1. **Clone the repository** and navigate to the project directory:

   ```bash
   git clone https://github.com/your-repo/AI_Tictactoe_Game.git
   cd AI_Tictactoe_Game
   ```

2. **Install Virtual Environment**:

   - For Windows:
     ```bash
     pip install virtualenv
     ```
   - For Linux/Mac:
     ```bash
     pip3 install virtualenv
     ```

3. **Create a Virtual Environment**:

   - For Windows:
     ```bash
     python -m venv venv
     ```
   - For Linux/Mac:
     ```bash
     python3 -m venv venv
     ```

4. **Activate the Virtual Environment**:

   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**:

   Install the required packages using the following command:

   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Game**:

   Start the game by running the following command:

   ```bash
   python runner.py
   ```

---

## How It Works

The game uses the **Minimax algorithm** to determine the AI's moves. The AI evaluates all possible moves and chooses the one that maximizes its chances of winning or forces a tie. The game supports:

1. **Player vs AI**: Play against the AI.

---

## Project Structure

- **`tictactoe.py`**: Contains the core game logic, including the Minimax algorithm, board state management, and win/draw detection.
- **`runner.py`**: The main script to run the game.
- **`requirements.txt`**: Lists the dependencies required to run the project.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to the branch.
4. Submit a pull request.

---

## Acknowledgments

- Inspired by the CS50 AI course.

---

Enjoy the game! 🎮
