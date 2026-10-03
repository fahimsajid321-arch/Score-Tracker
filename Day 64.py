class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def Add_book(self, new_book):
        if new_book not in self.books:
            self.books.append(new_book)
            self.no_of_books +=1
            print(f"New Book Named {new_book} has been added and total books are now {self.no_of_books}")

    def Names(self):
        for books in self.books:
            print(books)

    def total_books(self):
        print("Total books in Library are: ", self.no_of_books)


a = Library()
a.Add_book("What")
a.Add_book("What")
a.Add_book("is this")
a.Names()
a.total_books()





        