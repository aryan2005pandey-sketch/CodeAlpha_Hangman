import random

def hangman():
    # Predefined words
    words = ["python", "code", "alpha", "internship", "program"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("🎮 Welcome to Hangman!")
    print("Guess the word:", " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("\nEnter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("❗ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong! Attempts left: {attempts}")

        print("Word:", " ".join(guessed))

    if "_" not in guessed:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n😢 Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
  
