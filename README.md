
# Word Game
![Screenshot 2025-01-31 at 12 50 57 PM](https://github.com/user-attachments/assets/8e03302e-0e67-4075-98c0-f437ce929ce4)

## Introduction
This is a simple word-guessing game inspired by Wordle. The game allows players to guess a **seven-letter word**, providing feedback based on the correctness of their guesses.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Features](#features)
- [Files Overview](#files-overview)
- [License](#license)

## Installation
1. **Clone this repository**:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install dependencies** (if any):
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```sh
   python app.py
   ```

## Usage
- Run `app.py` to start the game.
- Players enter a seven-letter word as a guess.
- The game provides feedback:
  - **Green**: Correct letter in the correct position.
  - **Yellow**: Correct letter in the wrong position.
  - **Gray**: Letter is not in the word.

## Customization
You can modify the game settings to fit your preferences:

### Changing the Word Length
If you want to use a different word length instead of seven letters:
1. Replace the words in `common-7-letter-words.txt` with words of your desired length.
2. Ensure that all words in the file match the intended length to maintain consistency in gameplay.

### Adjusting the Difficulty
To change the number of allowed guesses:
1. Open `app.py` (or the relevant settings file).
2. Locate the `MAX_GUESSES` variable.
3. Modify its value to increase or decrease the number of allowed guesses:
   ```python
   MAX_GUESSES = 10  # Increase to allow more attempts
   ```
   A lower value makes the game harder, while a higher value makes it easier.

## Features
- Wordlist from `common-7-letter-words.txt`
- Interactive user interface (CSS-based design)
- Adjustable difficulty (via `MAX_GUESSES`)
- Flexible word length customization

## Files Overview
- **`app.py`** - Main script to run the game.
- **`words.py`** - Handles word selection and game logic.
- **`common-7-letter-words.txt`** - List of valid words.
- **`style.css`** - Styles the game interface.
- **`# Code Citations.md`** - MIT license and code references.

## Licenses, Sources & Acknowlegements
This project is licensed under the **MIT License** and based on Posit's
[ShinyLive Wordle Example](https://github.com/posit-dev/shinylive/tree/0cd59dce79a5c980943bba1c8a4af208e462f67b/examples/python/wordle/app.py). While I added in certain features, like the 7-word list, limitations on the number of guesses, and other behavior, much of the code is based on this excellent example from the Posit Team. To see this and other fun things you can do with Shiny, check out the [Shiny for Python Playground](https://shinylive.io/py/examples/)!
```
