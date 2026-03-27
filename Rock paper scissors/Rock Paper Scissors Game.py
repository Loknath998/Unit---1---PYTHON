import random
user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]
while True:
    print("\n--- Rock Paper Scissors ---")
    user_input = input("Enter Rock, Paper, or Scissors (or 'exit' to quit): ").lower()
    if user_input == "exit":
        break
    if user_input not in options:
        print("Invalid input! Please try again.")
        continue
    computer_choice = random.choice(options)
    print("Computer chose:", computer_choice)
    if user_input == computer_choice:
        print("Result: It's a Tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print("Result: You Win!")
        user_score += 1
    else:
        print("Result: Computer Wins!")
        computer_score += 1
print("\n--- Final Game Summary ---")
print("Your Total Score:", user_score)
print("Computer Total Score:", computer_score)
if user_score > computer_score:
    print("Final Result: You are the Champion!")
elif user_score < computer_score:
    print("Final Result: Computer is the Champion!")
else:
    print("Final Result: It's an overall Draw!")
print("Thank you for playing!")
