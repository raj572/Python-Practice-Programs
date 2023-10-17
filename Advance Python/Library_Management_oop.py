'''
1. Create a Class for a Library:
Design a class called Library that represents a library. It should have attributes like the library name, location, and a list of books. Implement methods for adding books to the library, borrowing books, and returning books. Create instances of the Library class and perform operations like adding books and borrowing/returning books.
'''
# class Library:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location
#         self.books = []

#     def add_book(self, book_title):
#         self.books.append(book_title)

#     def borrow_book(self, book_title):
#         if book_title in self.books:
#             self.books.remove(book_title)
#             return f"You have borrowed '{book_title}'."
#         else:
#             return f"'{book_title}' is not available in the library."

#     def return_book(self, book_title):
#         self.books.append(book_title)
#         return f"You have returned '{book_title}'."

#     def list_books(self):
#         return self.books

# # Create an instance of the Library class
# my_library = Library("My Library", "City Center")

# # Add books to the library
# my_library.add_book("Book 1")
# my_library.add_book("Book 2")
# my_library.add_book("Book 3")

# # Borrow and return books
# print(my_library.borrow_book("Book 2"))  
# print(my_library.return_book("Book 2"))  

# # List available books
# print("Available books:", my_library.list_books()) 
# my_library.borrow_book("Book 4")

class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []

    def add_book(self, book_title):
        self.books.append(book_title)

    def borrow_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
            return f"You have borrowed '{book_title}'."
        else:
            return f"'{book_title}' is not available in the library."

    def return_book(self, book_title):
        if book_title not in self.books:
            return f"'{book_title}' was not borrowed from this library."
        else:
            self.books.append(book_title)
            return f"You have returned '{book_title}'."
    def list_books(self):
        return self.books

def main():
    library_name = input("Enter the library name: ")
    library_location = input("Enter the library location: ")
    my_library = Library(library_name, library_location)

    while True:
        print("\nLibrary Menu:")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. List available books")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            book_title = input("Enter the title of the book to add: ")
            my_library.add_book(book_title)
            print(f"'{book_title}' has been added to the library.")

        elif choice == "2":
            book_title = input("Enter the title of the book to borrow: ")
            result = my_library.borrow_book(book_title)
            print(result)

        elif choice == "3":
            book_title = input("Enter the title of the book to return: ")
            result = my_library.return_book(book_title)
            print(result)

        elif choice == "4":
            available_books = my_library.list_books()
            print("Available books:", available_books)

        elif choice == "5":
            print("Thank you for using the library. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

