# print([x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0])

# ans = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
# print(ans)


# ans = []

# for x in range(1, 101):
#     if x % 3 == 0 and x % 5 == 0 :
#         ans.append(x)

# print(ans)


# ans = list(filter(lambda x : x % 3 == 0 and x % 5 == 0, range(1, 101)))
# print(ans)

# ans = list(range(15, 101, 15))
# print(ans)

# class student:
#     def __init__(self, name):
#         self.name = name
#         self.books = []

#     def show_books(self):
#         print(self.name, "has:", self.books)

# class Library:
#     def __init__(self):
#         self.books = []
    
#     def add(self, book):
#         self.books.append(book)
#         print(book, "added to library")

#     def issue_book(self, student, book):
#         if book in self.books:
#             self.books.remove(book)
#             student.books.append(book)
#             print(book, "issued to", student.name)
    
