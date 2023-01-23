class Bookshelf:
    def __init__(self,*books):
        self.books=books

    def __str__(self):
        return f"bookshelf with {len(self.books)} books"


class Book:
    def __init__(self,name):

        self.name=name
    def __str__(self):
        return f"Book {self.name}"

book=Book('Harry Potter')
book2=Book('python')
shelf=Bookshelf(book,book2)
print(shelf)
print(shelf.books)