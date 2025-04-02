


class Library:
    def __init__(self,name) -> None:
        self.name=name  
        self.book=[]
    def add_books(self,book1):
        self.book.append(book1.name)
        return self.book

class books:
    def __init__(self,name,year) -> None:
        self.name=name
        self.year=year

library1=Library("hello world")

book1=books("praksah","2024")
library1.add_books(book1)
print(library1.book)

