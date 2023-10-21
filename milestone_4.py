import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.list_of_guesses:
            print(f"You already guessed '{guess}'. Try again.")
            return False
        elif guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.list_of_guesses.append(guess)
            return True
        else:
            self.num_lives -= 1
            self.list_of_guesses.append(guess)
            return False

    def is_game_over(self):
        if self.num_lives <= 0:
            return True
        elif '_' not in self.word_guessed:
            return True
        else:
            return False

    def display_game_state(self):
        print(f"Word: {' '.join(self.word_guessed)}")
        print(f"Letters Guessed: {' '.join(self.list_of_guesses)}")
        print(f"Lives Remaining: {self.num_lives}")

    def play_game(self):
        while not self.is_game_over():
            self.display_game_state()
            guess = input("Guess a letter: ")
            self.check_guess(guess)
            
        if '_' not in self.word_guessed:
            print(f"Congratulations! You've guessed the word: {self.word}")
        else:
            print(f"Out of lives. The word was: {self.word}")

# Test the Hangman class
word_list = ['apple', 'mango', 'avocado', 'lemon', 'durian']
hangman_game = Hangman(word_list)
hangman_game.play_game()