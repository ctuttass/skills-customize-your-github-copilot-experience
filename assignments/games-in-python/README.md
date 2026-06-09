# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python, practising string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️	Set Up the Game

#### Description
Initialise all the variables needed before the game begins.

#### Requirements
Completed program should:

- Randomly select a secret word from the predefined word list using `random`
- Create an empty list or set to track guessed letters
- Set a starting count for incorrect guesses
- Define a maximum number of allowed incorrect guesses (e.g. 6)

### 🛠️	Implement the Game Loop

#### Description
Write the main loop that runs each round of the game, accepting player input and updating the game state.

#### Requirements
Completed program should:

- Display the current word progress using underscores for unguessed letters (e.g. `_ y _ _ o _`)
- Prompt the player to enter a single letter guess
- Check whether the guess is in the secret word and update progress or increment the incorrect guess count
- Display the number of incorrect guesses remaining after each turn
- Continue looping until the word is fully guessed or the player runs out of attempts

### 🛠️	Handle Win and Lose Conditions

#### Description
Detect when the game is over and display an appropriate message to the player.

#### Requirements
Completed program should:

- Display a congratulations message when the player guesses the full word
- Display a game-over message (including the secret word) when attempts are exhausted
- End the loop cleanly once either condition is met

