import random
import string

def get_word():
    """
    Returns a random word from the word list.
    """
    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    return random.choice(words).upper()

def play_hangman():
    word = get_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Print the current state of the game
        print(f"You have {lives} lives left and you have used these letters: {' '.join(used_letters)}")
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        # Get the user's guess
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in the word!")
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")

    # Game over
    if lives == 0:
        print(f"You died, sorry! The word was {word}")
    else:
        print(f"Congratulations! You guessed the word {word}!")

if __name__ == "__main__":
    play_hangman()