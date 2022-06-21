import random

# Generates a random word from the list
def generate_word(text):
    random_word = random.choice(text)
    print('WELCOME TO MYSTERY WORD! The computer has selected a random word.\n')
    print('Can you guess a letter in the word? \n ')
    return random_word  

# Displays the word to unveil
def display_word(text):
    word_to_unveil = str('_ '*len(text))
    print(word_to_unveil)
    return word_to_unveil

def user_guess(text):
    guess = input()    

def play_game():
    #Reads in the text as a list
    with open("words.txt") as file:
        read_file = file.read()
        read_file_list = read_file.split()
    # Generate random word
    random_word = generate_word(read_file_list)
    # Display word to unveil
    word_to_guess = display_word(random_word)
    # Asks user for input of a letter
    user_guess(word_to_guess)


if __name__ == "__main__":
    play_game()
