### Objectives
## Create an interactive Program
- Create a word-guessing game called 'Mystery Word' where the player plays against the computer
- Game will run on command line as a text-only interactive game

## Read from a file
- words.txt will be the source file game will use to choose the secret word
- test-word.txt file will be only 1 word, used to test the program
- 

## Choose a random value
- The computer selects a word at random from the list of words in the words.txt file
- Computer lets user know how many letters the secret word contains at the start

## Keep track of the state
- Ask user to supply one guess per round, upper or lower case
    - If a user guesses wrong, they lose a guess. They have 8 wrong guesses
    - If a user guesses the same letter twice, do not take a guess away
        - Print a message letting them know they've already guessed that letter
- Game ends when the player runs out of guesses or constructs the full word.
    - Reveal the word if they don't get it
    - 
