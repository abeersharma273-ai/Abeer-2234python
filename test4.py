class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(self.title, "has been borrowed successfully.")
        else:
            print(self.title, "is already borrowed.")

    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print(self.title, "has been returned successfully.")
        else:
            print(self.title, "is already available.")

    def show(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Borrowed:", self.is_borrowed)
        print("------------------------")


# Creating at least 3 Book objects
book1 = Book("Python Programming", "John")
book2 = Book("Data Science", "David")
book3 = Book("Computer Basics", "Robert")

# Display book details
book1.show()
book2.show()
book3.show()

# Borrow books
book1.borrow()
book2.borrow()

# Return a book
book1.return_book()

# Demonstrate borrowing and returning another book
book3.borrow()
book3.return_book()

# Display final status
print("\nFinal Book Status:")
book1.show()
book2.show()
book3.show()
