import random

def hangman():
    words = ["neymar", "ronaldo", "messi", "mbappe", "salah"]
    word = random.choice(words)
    guessed = []
    tries = 6

    print("Welcome to Hangman!")
    while tries > 0:
        display = ""
        for letter in word:
            if letter in guessed:
                display += letter
            else:
                display += "_"
        print("Word:", display)
        
        if "_" not in display:
            print("Congratulations! You won!")
            break

        guess = input("Guess a letter: ").lower()
        if guess in guessed:
            print("You already guessed that letter.")
        elif guess in word:
            guessed.append(guess)
            print("Good guess!")
        else:
            guessed.append(guess)
            tries -= 1
            print(f"Wrong guess. You have {tries} tries left.")

    if tries == 0:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
