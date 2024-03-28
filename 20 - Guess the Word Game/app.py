import random

def get_word():
    words = ["python", "programming", "computer", "science", "algorithm",
             "database", "network", "software", "developer", "interface"]
    return random.choice(words)

def play_game():
    word = get_word()
    word_length = len(word)
    hidden_word = ["_"] * word_length
    attempts = 6
    guessed_letters = []

    print("Welcome to Guess the Word!")
    print(f"The word has {word_length} letters.")
    print(" ".join(hidden_word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Correct guess!")
            for i in range(word_length):
                if word[i] == guess:
                    hidden_word[i] = guess
            print(" ".join(hidden_word))
            
            if "_" not in hidden_word:
                print("Congratulations! You guessed the word!")
                return
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
    
    print("Game over! You ran out of attempts.")
    print(f"The word was: {word}")

# Start the game
play_game()