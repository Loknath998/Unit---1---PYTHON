score = 0

print("----- General Knowledge Quiz -----")
print("Choose the correct option: A, B, C, or D")
print("\n1. Which is the largest planet in our solar system?")
print("A. Earth  B. Jupiter  C. Mars  D. Saturn")
ans = input("Your Answer: ").upper()
if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is B.")
print("\n2. Who wrote the play 'Romeo and Juliet'?")
print("A. Charles Dickens  B. Mark Twain  C. William Shakespeare  D. J.K. Rowling")
ans = input("Your Answer: ").upper()
if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is C.")
print("\n3. What is the chemical symbol for Water?")
print("A. CO2  B. O2  C. H2O  D. NaCl")
ans = input("Your Answer: ").upper()
if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is C.")
print("\n4. Which country is known as the Land of the Rising Sun?")
print("A. China  B. Japan  C. South Korea  D. Thailand")
ans = input("Your Answer: ").upper()
if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is B.")
print("\n5. What is the capital of France?")
print("A. Berlin  B. Madrid  C. Rome  D. Paris")
ans = input("Your Answer: ").upper()
if ans == "D":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is D.")
print("\n6. Which gas do plants absorb from the atmosphere?")
print("A. Oxygen  B. Nitrogen  C. Carbon Dioxide  D. Hydrogen")
ans = input("Your Answer: ").upper()
if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is C.")
print("\n7. Who painted the Mona Lisa?")
print("A. Vincent van Gogh  B. Pablo Picasso  C. Leonardo da Vinci  D. Claude Monet")
ans = input("Your Answer: ").upper()
if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is C.")
print("\n8. Which is the smallest continent by land area?")
print("A. Africa  B. Australia  C. Europe  D. Antarctica")
ans = input("Your Answer: ").upper()
if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is B.")
print("\n9. What is the hardest natural substance on Earth?")
print("A. Gold  B. Iron  C. Diamond  D. Graphite")
ans = input("Your Answer: ").upper()
if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is C.")
print("\n10. Which organ is responsible for pumping blood in the human body?")
print("A. Lungs  B. Brain  C. Heart  D. Kidney")
ans = input("Your Answer: ").upper()
if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is C.")
print("\n----- Quiz Results -----")
print("Total Questions: 10")
print("Your Score:", score)
