import random
from re import U

#Reads in the file and selects a random word
with open("words.txt") as file:
    read_file = file.read()
    read_file_list = read_file.split()
    random_word = random.choice(read_file_list)

    print(random_word)
    print(f'WELCOME TO THE MYSTERY WORD GAME.')
    print(f'The computer has generated a word with {len(random_word)} letters. You have 8 tries to guess it!\n')
    word_to_unveil = list('_'*len(random_word))
    print(' '.join(word_to_unveil))

#Function to ask for an input
def guess_letter(text):
    while True:
        guess = input("Can you guess a letter in the word?\n")
        if len(guess) == 1 and guess.isalpha():
            break
        print("\nSorry, invalid input. Just 1 letter please.")
    return guess

#Function to play the game
def play_game():
    already_guessed = []
    turns = 0

    while turns < 8:
        user_guess = guess_letter(random_word)
        #checks to see if guess is in the word
        for index, letter in enumerate(random_word):
            if letter == user_guess:
                already_guessed.append(user_guess)
                word_to_unveil[index] = user_guess
                print(f'{user_guess} is in the word!')
        #checks to see if guess is not in the word/already guessed
        if user_guess not in already_guessed:
            already_guessed.append(user_guess)
            print(f'\n{user_guess} is not in the word.')
            turns += 1
            print(f'You have {8-turns} turns left!')
        #lets user know if guess has been guessed
        if user_guess in already_guessed:
            print(f'You already guessed {user_guess}')
        print(' '.join(word_to_unveil))
                #checks to see if word is filled in
        if ''.join(word_to_unveil) == random_word:
            print("Congrats, you've won! You filled the word in correctly.")
            break
    print(f'The word was {random_word}.')



if __name__ == "__main__":
    play_game()
