import random

# List of 5 predefined words
words = ["apple", "tiger", "python", "school", "computer"]

# Select a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Maximum incorrect guesses
incorrect_guesses = 0
max_guesses = 6

# Store letters already guessed
guessed_letters = []

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

while incorrect_guesses < max_guesses and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check whether letter is in the word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Game result
if "_" not in guessed_word:
    print("\n🎉 You won!")
    print("The word was:", word)
else:
    print("\n❌ You lost!")
    print("The word was:", word)