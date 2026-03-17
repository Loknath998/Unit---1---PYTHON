print("=" * 40)
print("    BINARY SEARCH GUESSING ENGINE")
print("=" * 40)
print("Think of a number between 1 and 100.")
print("The computer will find it in 7 steps or less.\n")
low = 1
high = 100
attempts = 0
while low <= high:
    mid = (low + high) // 2
    attempts += 1
    print(f"Attempt #{attempts}: I guess {mid}")
    print(f"Current Search Range: [{low} - {high}]")
    feedback = input("Feedback -> (H)igh, (L)ow, or (C)orrect: ").upper()
    if feedback == 'C':
        print("\n" + "*" * 40)
        print(f" LOGIC SUCCESS: Found {mid} in {attempts} steps!")
        print("*" * 40)
        break
    elif feedback == 'H':
        high = mid - 1
    elif feedback == 'L':
        low = mid + 1
    else:
        print(">> Error: Please enter H, L, or C only.")
        attempts -= 1 
if low > high:
    print("\n[!] Logic Error: Your answers were inconsistent.")
    print("The search range has collapsed. Please try again!")
