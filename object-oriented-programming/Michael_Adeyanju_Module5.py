# book - store details about aweJBV book and check whester its available 
# library - manages a collection of books 
# member - rep a user who can borrow Book

class Book :
    def __init__(self, title, author, price, is_available):
        self.title = title
        self.author = author
        self.price = price
        self.is_available = is_available
hv
class Library :
    books = []
    def __init__(self):
        self.books = []
    def list_of_books(self):
        print('List of books : ')
        if not self.books:
            print('The library is empty')
        for x in self.books :
            print(f' * {x.title} by {x.author} at the rate of ${x.price}\n')

    def add_book(self, book):
        self.books.append(book)
        Library.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f'Error : "{book.title} is not in the library!!')

    def search_by_author(self, author):
        for x in self.books:
            if x.author == author:
                print(f'Found: {x.title} by {x.author}')
            else :
                print(f'No books by {author} found')
    @classmethod
    def total_of_books(cls):
        total = len(cls.books)
        print(f'Total of all books in the library : {total}')
    @staticmethod
    def validate(title):
        if title:
            print(f' "{title}" is a valid title')
        else :
            print('Error: the book title is empty')



class Member :
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, library, book_title):
        for x in library.books:
            if x.title == book_title:
                if x.is_available:
                    x.is_available = False
                    self.borrowed_books.append(x)
                else:
                    print(f'Sorry , {x.title} is already borrowed')
                return
            
    def return_book(self, library, book_title):
        for x in library.books:
            if x.title == book_title:
                x.is_available = True
                self.borrowed_books.remove(x)
                print(f'Successfully returned {x.title}')


lib = Library()

b1 = Book('inter', 'mike', 4000, True)
b2 = Book('anywhere', 'kunle', 500, True)
b3 = Book('oliver twist', 'kenny', 10000, True)
# add books to the library
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

m1 = Member('Michael')
m1.borrow(lib, 'inter')


# ----- start summary--------

print('\nAll Books in library: ')
for x in lib.books:
    status = 'Available' if x.is_available else 'Borrowed'
    print(f' - {x.title} ({status})')

print()
print('\n Borrowed List: ')
all_members = [m1]
for x in all_members:
    borrowed_titles = [book.title for book in x.borrowed_books]
    print(f' - {x.name} has: {borrowed_titles}')

print()
print('\n Available books : ')
for x in lib.books:
    if x.is_available:
        print(f' - {x.title}')

print('---------------------------\n')




        




