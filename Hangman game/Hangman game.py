word = "python"
guesses = ""
turns = 6

print("--- Welcome to Hangman ---")
print("Guess the secret word one letter at a time.")

while turns > 0:
    failed = 0
    
    print("\nWord: ", end="")
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    
    if failed == 0:
        print("\n\n" + "="*20)
        print("CONGRATS! YOU WIN!")
        print("="*20)
        break

    guess = input("\nGuess a letter: ").lower()
    guesses += guess

    if guess not in word:
        turns -= 1
        print(f"Wrong! You have {turns} more guesses left.")

if turns == 0:
    print("\n" + "-"*20)
    print("GAME OVER")
    print(f"The secret word was: {word}")
    print("-"*20)
