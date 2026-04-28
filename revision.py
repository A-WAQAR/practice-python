print([x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0])

ans = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(ans)


ans = []

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0 :
        ans.append(x)

print(ans)


ans = list(filter(lambda x : x % 3 == 0 and x % 5 == 0, range(1, 101)))
print(ans)

ans = list(range(15, 101, 15))
print(ans)

class student:
    def __init__(self, name):
        self.name = name
        self.books = []

    def show_books(self):
        print(self.name, "has:", self.books)

class Library:
    def __init__(self):
        self.books = []
    
    def add(self, book):
        self.books.append(book)
        print(book, "added to library")

    def issue_book(self, student, book):
        if book in self.books:
            self.books.remove(book)
            student.books.append(book)
            print(book, "issued to", student.name)
        else:
            print(book, "not available")

    def return_book(self, student, book):
        if book in student.books:
            student.books.remove(book)
            self.books.append(book)
            print(book, "returned by", student.name)
        else:
            print(student.name, "does not have this book")

    def show_library_books(self):
        print("library books: ", self.books)

lib = Library()
s1 = student("asif")

lib.add("python")
lib.add("SQL")
lib.add("Django")

lib.show_library_books()

lib.issue_book(s1, "python")

lib.show_library_books()
s1.show_books()

lib.return_book(s1, "python")

lib.show_library_books()
s1.show_books()
         



    
