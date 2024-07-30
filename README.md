# Snake-Gun-Water Game

Welcome to the Snake-Gun-Water Game repository! This project features two implementations of a classic game where you choose between Snake, Gun, and Water, and compete against the computer.

## Game Description

In this game:
- **Snake** (s) beats **Water** (w)
- **Gun** (g) beats **Snake** (s)
- **Water** (w) beats **Gun** (g)

The game is a fun twist on the traditional Rock-Paper-Scissors, integrating three unique choices with a randomized computer opponent.

## Features

- **User vs. Computer**: Play against a computer that makes random choices.
- **Two Implementations**: Two versions of the game with different logic for determining the winner.

## Files

### `main.py`

This script implements the basic version of the game where:
- It defines the choices: Snake, Gun, and Water.
- It compares the user's choice with the computer's choice to determine the winner using straightforward conditional checks.

### `main_short_version.py`

This script implements a more concise version of the game where:
- It uses a simplified logic to determine the winner by calculating differences between choices.
- The outcome is based on modular arithmetic to decide the result.

## Installation

To get started with the Snake-Gun-Water Game, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shubhambhosle798/snake-gun-water_game.git
2. **Navigate to the Project Directory**:
   ```bash
   cd snake-gun-water_game
   ```
3. **Run the Game:**
   Execute one of the Python scripts using Python 3:
   ```bash
   python main.py
   ```
   or
   ```bash
   python main_short_version.py
   ```

## Usage

1. **Start the Game**:
   Run the desired Python script to start the game.

2. **Controls**:
   Enter your choice between S (Snake), G (Gun), or W (Water).

3. **Objective**:
   Choose an option and see if you win, lose, or draw against the computer.

## Contributing
Contributions to the Snake-Gun-Water Game project are welcome! If you have ideas for improvements or find any issues, feel free to open an issue or submit a pull request.

## Contact
For any questions or feedback, please reach out to bhosleshubham798@gmail.com or open an issue in the repository.

## Thank you for visiting the Snake-Gun-Water Game repository:)
