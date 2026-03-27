while True:
    print("\n----- File Notes Saver -----")
    print("1. Write a New Note")
    print("2. Read Saved Notes")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        note = input("Enter your note: ")
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        print("Note saved successfully!")
    elif choice == '2':
        print("\n--- Your Saved Notes ---")
        try:
            with open("notes.txt", "r") as f:
                content = f.read()
                if content:
                    print(content)
                else:
                    print("Note file is empty.")
        except FileNotFoundError:
            print("Error: No notes found. Create one first!")
    elif choice == '3':
        print("Exiting System. Goodbye!")
        break
    else:
        print("Invalid Option. Please try again.")
