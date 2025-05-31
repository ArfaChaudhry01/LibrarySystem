# Project 2: Library Book Management System

books = {
    "Life Strategies": {"author": "Phillip C.", "available": True},
    "48 Powers of Law": {"author": "Peterson", "available": True},
    "Intelligent Investor": {"author": "Kevin", "available": True},
}

borrowed_books = []


def view_books():
    print("\n📚 Available Books:")
    for title, details in books.items():
        status = "Available ✅" if details["available"] else "Borrowed "
        print(f'"{title}" by {details["author"]} - {status}')
    print()


def borrow_book():
    book_title = input("Enter the book title to borrow: ").strip().lower()
    for title in books:
        if title.lower() == book_title:
            if books[title]["available"]:
                books[title]["available"] = False
                borrowed_books.append(title)
                print(f' You have borrowed "{title}".')
            else:
                print(f'"{title}" is already borrowed.')
            return
    print("Book not found in the library.")


def return_book():
    book_title = input("Enter the book title to return: ").strip().lower()
    for title in books:
        if title.lower() == book_title:
            if not books[title]["available"]:
                books[title]["available"] = True
                if title in borrowed_books:
                    borrowed_books.remove(title)
                print(f'✅ You have returned "{title}".')
            else:
                print(f'⚠️ "{title}" was not borrowed.')
            return
    print("Book not found in the library.")


def add_book():
    title = input("Enter the book title: ").strip()
    author = input("Enter the author's name: ").strip()
    if title in books:
        print("Book already exists in the library.")
    else:
        books[title] = {"author": author, "available": True}
        print(f'Book "{title}" by {author} added to the library.')


def view_borrowed_books():
    if not borrowed_books:
        print("\n No books currently borrowed.")
    else:
        print("\n Borrowed Books:")
        for title in borrowed_books:
            print(f'- "{title}"')
    print()


def main():
    print("Welcome to the Library System!")

    while True:
        print("\nMenu:")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add New Book")
        print("5. View Borrowed Books")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            view_books()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            add_book()
        elif choice == "5":
            view_borrowed_books()
        elif choice == "6":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
