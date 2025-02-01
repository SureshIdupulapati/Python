import random

# Hangman stages (if `hangman_stages.py` is missing)
hangman_stages = [
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
         |
    --------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
         |
    --------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
         |
         |
    --------
    """,
    """
      -----
      |   |
      O   |
     /|   |
         |
         |
    --------
    """,
    """
      -----
      |   |
      O   |
      |   |
         |
         |
    --------
    """,
    """
      -----
      |   |
      O   |
         |
         |
         |
    --------
    """,
    """
      -----
      |   |
          |
         |
         |
         |
    --------
    """
]

# Word list
words = ["apple", "banana", "cat", "dog", "elephant", "fish", "goat", "himalaya", "idly",
         "jungle", "king", "lemon", "monkey", "neck", "oppo", "plane", "queen", "ring",
         "sun", "tea", "umbrella", "van", "wonder", "yax", "zebra"]

# Choose a random word
guess_word = random.choice(words).lower()
word_length = len(guess_word)
empty_list = ["_"] * word_length  # Underscores for missing letters
attempts = 6  # Number of lives
guessed_letters = set()  # Track guessed letters
game_over = False

print("\n🎉 Let's Play Hangman! 🎉")
print("You have 6 lives. Try to guess the word letter by letter.")
print("Good luck!\n")
print(" ".join(empty_list))  # Display initial blank word

# Game loop
while not game_over:
    guess_letter = input("\nGuess a letter: ").lower()

    # Input validation
    if len(guess_letter) != 1 or not guess_letter.isalpha():
        print("⚠️ Please enter a single valid letter.")
        continue

    # Check if letter was already guessed
    if guess_letter in guessed_letters:
        print(f"⚠️ You've already guessed '{guess_letter}'. Try another letter.")
        continue
    guessed_letters.add(guess_letter)

    # Check if guess is correct
    if guess_letter in guess_word:
        for i in range(word_length):
            if guess_word[i] == guess_letter:
                empty_list[i] = guess_letter
        print("\n✅ Correct guess!")
    else:
        attempts -= 1
        print(f"\n❌ Wrong guess! '{guess_letter}' is not in the word. {attempts} lives left.")

    # Show current word progress
    print(" ".join(empty_list))

    # Show hangman stage
    print(hangman_stages[attempts])

    # Win condition
    if "_" not in empty_list:
        game_over = True
        print("\n🎉 Congratulations! You guessed the word correctly! 🎉")
        break

    # Lose condition
    if attempts == 0:
        game_over = True
        print("\n💀 Game Over! You lost all your lives.")
        print(f"The word was: {guess_word}")
