library = {}

while True:
    print("\n----- Library Menu -----")
    print("1. Add New Book")
    print("2. View Inventory")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        isbn = input("Enter ISBN: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        library[isbn] = {'title': title, 'author': author, 'status': 'Available'}
        print("Book added successfully!")
    elif choice == 2:
        print("\n--- Library Inventory ---")
        if not library:
            print("No books in system.")
        else:
            for isbn, info in library.items():
                print(f"ISBN: {isbn} | Title: {info['title']} | Status: {info['status']}")
    elif choice == 3:
        isbn = input("Enter ISBN to borrow: ")
        if isbn in library:
            if library[isbn]['status'] == 'Available':
                library[isbn]['status'] = 'Borrowed'
                print("Book issued successfully.")
            else:
                print("Error: Book is already borrowed.")
        else:
            print("Error: ISBN not found.")
    elif choice == 4:
        isbn = input("Enter ISBN to return: ")
        if isbn in library:
            library[isbn]['status'] = 'Available'
            print("Book returned successfully.")
        else:
            print("Error: Invalid ISBN.")
    elif choice == 5:
        print("Thank you for using the Library System!")
        break
    else:
        print("Invalid choice! Please try again.")
