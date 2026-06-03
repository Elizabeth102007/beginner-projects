class Book:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} ({self.pages} pages)"
    
    def __eq__(self, another):
        return self.pages == another.pages
    
    def __lt__(self, another):
        return self.pages < another.pages

    def __gt__(self, another):
        return self.pages > another.pages
    
b1 = Book("Atomic Habits", 350)
b2 = Book("Rich Dad Poor Dad", 300)
b3 = Book("Working with Emotional Intelligence", 400)

print(b1>b2)