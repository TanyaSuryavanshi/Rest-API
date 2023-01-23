class Bookshelf:
    def __init__(self,quantity):
        self.quantity=quantity

    def __str__(self):
        return f"bookshelf with {self.quantity} books"

shelf=Bookshelf(300)
print(shelf)
class Book(Bookshelf):
    def __init__(self,name,quantiy):
        super().__init__(quantiy)
        self.name=name
    def __str__(self):
        return f"Book {self.name}"

book=Book('Harry Potter',300)
print(book)