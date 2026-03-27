import random

print("="*30)
print("  DICE ROLLING CHALLENGE")
print("="*30)

while True:
    input("\nPress Enter to roll the dice...")
    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)
    
    print(f"Your Roll: {player_roll}")
    print(f"Computer's Roll: {computer_roll}")
    
    if player_roll > computer_roll:
        print("Result: >>> YOU WIN! <<<")
    elif computer_roll > player_roll:
        print("Result: >>> COMPUTER WINS! <<<")
    else:
        print("Result: >>> IT'S A TIE! <<<")
    play_again = input("\nRoll again? (y/n): ").lower()
    if play_again == 'n':
        print("Thanks for playing! Final scores saved.")
        break
