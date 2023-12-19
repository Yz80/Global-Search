class HangmanGame:
    def __init__(self, secret_word):
        self.secret_word = secret_word.upper()
        self.guesses = []
        self.incorrect = []
        self.max_attempts = 5
        self.attempts_left = self.max_attempts

    def display_word(self):
        display = ""
        for letter in self.secret_word:
            if letter in self.guesses:
                display += letter
            else:
                display += "_"
        return display
    def make_guess(self, guess):
        guess = guess.upper()
        if guess in self.secret_word and guess in self.guesses:
            print('Already guessed that')
        elif guess in self.secret_word and guess not in self.guesses:
            self.guesses.append(guess)
            return True
        elif guess not in self.secret_word and guess not in self.incorrect:
            self.incorrect.append(guess)
            self.attempts_left -= 1
            print(f"Wrong guess! Attempts left: {self.attempts_left}")
            return False
        elif guess not in self.secret_word and guess in self.incorrect:
            print('Already guessed that')