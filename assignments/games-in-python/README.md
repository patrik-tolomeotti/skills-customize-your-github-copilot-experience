# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python to practice string manipulation, loops, conditionals, and random selection. You will create an interactive word-guessing game that tracks player progress and handles win/lose conditions.

## 📝 Tasks

### 🛠️	Create the Hangman Game Logic

#### Description
Write a Python program that randomly selects a word from a predefined list. The player will guess letters to try to reveal the word before running out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a list of at least five words
- Accept letter guesses from the user
- Display the current progress (e.g., `_ a _ _ m a n`)
- Track and display the number of incorrect guesses remaining
- End the game when the word is guessed or attempts are exhausted
- Show a win or lose message at the end

**Example:**
```text
Word: _ a n g m a n
Guesses left: 3
Guessed letters: a, n, g, m
```

### 🛠️	Add Replay and Input Validation

#### Description
Enhance your game by allowing players to play again and by validating user input to ensure only single letters are accepted.

#### Requirements
Completed program should:

- Prompt the user to play again after each game
- Validate that each guess is a single alphabetical character
- Ignore repeated guesses and notify the player
- Reset the game state for each new round

**Example:**
```text
Invalid input! Please enter a single letter.
You've already guessed "a". Try a different letter.
Play again? (y/n)
```
