import random

#Reads in the file and selects a random word
with open("words.txt") as file:
    read_file = file.read()
    read_file_list = read_file.split()
    random_word = random.choice(read_file_list)

    print("WELCOME TO THE MYSTERY WORD GAME. The computer has generated a word!\n")
    word_to_unveil = list('_'*len(random_word))
    print(random_word)
    print(' '.join(word_to_unveil))

#Function to ask for an input
def guess_letter(text):
    while True:
        guess = input("\nCan you guess a letter in the word?\n")
        # if guess.isdigit() != True:
        #     break
        # print("\nSorry, no numbers!")
        if len(guess) == 1:
            break
        print("\nSorry, only 1 character at a time.")
    return guess

#Function to play the game
def play_game():
    # Asks user for input of a letter
    user_guess = guess_letter(random_word)
    for index, letter in enumerate(random_word):
        if letter == user_guess:
            word_to_unveil[index] = user_guess
            print(' '.join(word_to_unveil))
    if user_guess not in random_word:
            print("nope!")
    play_game()

if __name__ == "__main__":
    play_game()
