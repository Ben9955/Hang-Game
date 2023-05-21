# Hangman Game

This code is a simple implementation of the classic Hangman game in Python. The computer selects a random word from a predefined list, and the player needs to guess the word by choosing letters one by one.

## How to Play

1. Run the script in a Python environment.
2. The computer will randomly select a word from the provided word list.
3. Enter a letter to guess the word. You can only enter one letter at a time.
4. If the letter is present in the word, it will be revealed in the word's current state.
5. If the letter is not in the word, you will lose a guess.
6. Keep guessing letters until you either guess the word correctly or run out of guesses.
7. If you guess the word correctly, you win! You can choose to play again.
8. If you run out of guesses, it's game over. You can choose to play again.

## Word Difficulty Levels

The game offers three difficulty levels: easy, medium, and difficult. The number of guesses you have depends on the difficulty level you choose. The available difficulty levels are:

- Easy: 25 guesses
- Medium: 15 guesses
- Difficult: 8 guesses

## Additional Notes

- The game only accepts single letter inputs. If you enter more than one letter, you will be prompted to enter a single letter.
- Non-alphabetic characters are not accepted as valid inputs.
- The word list can be customized by modifying the `words` variable in the code.
- After each game, you will be asked if you want to continue playing. Enter "yes" to play again or "no" to exit the game.

Enjoy playing Hangman!
