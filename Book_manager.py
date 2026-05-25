class Book:
    def __init__(self, title: str, author: str, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False
    
    def __str__(self):
        return f"Title: {self.title.title()} | Author: {self.author.title()} | Pages: {self.pages} | {'Long Read!' if self.is_long() else 'Short Read!'}"

book_1 = Book("rich dad poor dad", "robert kiyosaki", 291) 
book_2 = Book("atomic habits", "james clear", 350)

print(book_1)
print(book_2)