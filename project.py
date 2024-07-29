class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books_info = self.file.read().splitlines()
        if not books_info:
            print("No books found.")
        else:
            for book_info in books_info:
                book_details = book_info.split(",")
                book_title, author, release_year, num_pages = book_details
                print(f"Book name: {(book_title)} \nAuthor: {author}")


    def add_book(self):
        book_title = input("Enter book title: ")
        author = input("Enter author: ")
        release_year = input("Enter first release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{book_title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"{book_title} added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        books_info = self.file.readlines()

        book_found = False
        for i, book_info in enumerate(books_info):
            if title_to_remove in book_info:
               book_found = True
               del books_info[i]  
               break

        if book_found:
            self.file.seek(0)
            self.file.truncate()

            for book_info in books_info:
                self.file.write(book_info)

            print(f"{title_to_remove} removed successfully.")
        else:
            print("Book isn't found.")

    

lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")
