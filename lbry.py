class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        books = []
        with open(self.file_name, "r") as file:
            for line in file:
                books.append(line.strip().split(","))
        for book in books:
            print(f"Title: {book[0]}\nAuthor: {book[1]}\nRelease Year: {book[2]}\nPages: {book[3]}\n ")
            print("----------------------------------------")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)

    def remove_book(self):
        title = input("\nEnter book title to remove: ")
        books = []
        with open(self.file_name, "r") as file:
            for line in file:
                books.append(line.strip().split(","))
        index = -1
        for i, book in enumerate(books):
            if book[0] == title:
                index = i
                break
        if index != -1:
            del books[index]
            with open(self.file_name, "w") as file:
                for book in books:
                    file.write(",".join(book) + "\n")
            print(f"\nBook '{title}' removed successfully.")
        else:
            print(f"\nBook '{title}' not found in the library.")


if __name__ == "__main__":
    lib = Library()
    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("q) Exit")
        choice = input("\nEnter your choice: ")

        if choice.lower() == "q":
            break
        elif choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        else:
            print("\nInvalid choice. Please try again.")

