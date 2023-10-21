# Create a class called hangman
import random

class hangman:
    def __init__(self, word_list, num_lives=5):
        #initialise attributes
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        # convert the guessed letter to lower case
        guess = guess. lower()

        # create an if statement that checks if the guess is in the word
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
        
            self.num_letters -= 1

        else:
            pass
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter:")

            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

# Test the hangman class
hangman_game = hangman(["apple", 'banana', 'cherry'])
hangman_game.ask_for_input()