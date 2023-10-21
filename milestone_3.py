import random
word_list =  ['mangosteen', 'mango', 'avocado', 'lemon', 'durian']
word = random.choice(word_list)

# Define a function called 'check_guess'
def check_guess(guess, word):
    # Convert the guess to lowercase
    guess = guess.lower()
    # Check if the guess is in the word
    if guess in word: 
    # Print a message for a correct guess
        print(f"Good guess! '{guess}' is in the word.")
    else:
        # Print a message for an incorrect guess
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    while True:
        # Ask the user to guess a letter
        guess = input("Guess a letter: ")

        if guess.isalpha() and len(guess) == 1:
            check_guess(guess, word)
            # If the guess passes the checks, break out of the loop
            break
        else:
            # If the guess does not pass the checks, print a message.
            print("Invalid letter. Please, enter a single alphabetical character")

def congratulate(word):
    if set(word) == set(word.lower()):
        print(f"Congratulations! You've guessed the word: {word}")
    else: 
        print(f"Randomly chosen word: {word}")

ask_for_input()


