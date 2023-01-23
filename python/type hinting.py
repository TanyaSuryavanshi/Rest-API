from typing import List
class Book:
    pass

class Bookshelf:
    def __init__(self,books: List[Book]):
        self.books=books

    def __str__(self) -> str:
        return f"bookshelf with {len(self.books)} books"
shelf=Bookshelf(['Harry Potter','python','me'])
print(shelf)