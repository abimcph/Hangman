# Import the random module
import random

# Create a list of favorite fruits and assign to a variable named word_list
word_list =  ['mangosteen', 'mango', 'avocado', 'lemon', 'durian']

# Generate a random word from the word_list
word = random.choice(word_list)
print(word)

# Ask the user to enter a single letter
guess = input("Please enter a single letter: ")

# Check that the input is a single character
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

print("Randomly chosen word:", word)
print("User's guess:", guess)