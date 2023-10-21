# Create a while loop and set the condition to True. Setting the condition to True ensures that the code runs continuously. 
while True: 
    # Ask the user to guess a letter
    guess = input("Guess a letter: ")

    # Check if the guess is a single alphabetical character
    if guess.isalpha() and len(guess) == 1:
        # If the guess passes the checks, break out of the loop
        break
    else:
        # If the guess does not pass the checks, print a message.
        print("Invalid letter. Please, enter a single alphabetical character")

# Check if the guess is in the word
if guess in secret_word: 
    # Print a message for a correct guess
    print(f"Good guess! '{guess}' is in the word.")
else:
    # Print a message for an incorrect guess
    print(f"Sorry, '{guess}' is not in the word. Try again.")

# Define a function called 'check_guess'
def check_guess(guess):
    # Convert the guess to lowercase
    guess = guess.lower()
    # Check if the guess is in the word
    if guess in secret_word: 
    # Print a message for a correct guess
        print(f"Good guess! '{guess}' is in the word.")
    else:
        # Print a message for an incorrect guess
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# Define a function called 'ask_for_input'
def ask_for_input():
    while True:
        # Ask the user to guess a letter
        guess = input("Guess a letter: ")

        check_guess(guess)

        # Check if the word has been guessed
        if word_is_guessed():
            print("Congratulations! You've guessed the word.")
ask_for_input()