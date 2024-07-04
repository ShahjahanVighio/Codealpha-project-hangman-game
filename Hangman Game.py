import random

# List of words to choose from
word_list = ['python', 'javascript', 'hangman', 'developer', 'algorithm', 'function']


# Function to choose a random word from the list
def get_random_word():
    return random.choice(word_list)


# Function to display the current state of the word being guessed
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])


# Main function to run the Hangman game
def hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = set()
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")

    while len(incorrect_guesses) < max_incorrect_guesses and set(word) != guessed_letters:
        print("\nCurrent word:", display_word(word, guessed_letters))
        print("Incorrect guesses:", ', '.join(incorrect_guesses))
        print(f"You have {max_incorrect_guesses - len(incorrect_guesses)} incorrect guesses left.")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.add(guess)
            print(f"Sorry, '{guess}' is not in the word.")

    if set(word) == guessed_letters:
        print("\nCongratulations! You've guessed the word:", word)
    else:
        print("\nSorry, you've run out of guesses. The word was:", word)


if __name__ == "__main__":
    hangman()
