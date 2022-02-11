# Create a book class. Initialise each book object with 
# author, title, ISBN, publication year, number of pages. 
# Define str method which displays information about the book.
# Define search method which searches by book or by author, 
# through a dictionary attribute of the class which tracks the book objects created. 
# Define two subclasses for different genres of books which override the default str method. 


class Book():

    books = {}

    def __init__(self, author, title, isbn, year, pages):
        self.author = author.title()
        self.title = title.title()
        self.isbn = isbn
        self.year = year
        self.pages = pages
        if self.author in Book.books:
            Book.books[self.author].append(self)
        else: 
            Book.books[self.author]=[self]

    @staticmethod
    def search(search_term):
        search_term = search_term.title()
        if search_term in Book.books.keys():
            results = Book.books.get(search_term, [])
            return f'Books by {search_term}: {", ".join([book.title for book in results]) if results else "None"}'
        else:
            for author, books in Book.books.items():
                if search_term in [book.title for book in books]:
                    return f"{search_term} is written by {author}."
            return "Not found."

    def __str__(self):
        return f'"{self.title}" by {self.author}\nPublication year: {self.year}\nNumber of pages: {self.pages}\nISBN: {self.isbn}\n'

class SelfHelpBook(Book):
    def __str__(self):
        return f'Self-help book "{self.title}" by {self.author}\nPublication year: {self.year}\nNumber of pages: {self.pages}\nISBN: {self.isbn}\n'

class FantasyNovel(Book):
    def __str__(self):
        return f'Fantasy novel "{self.title}" by {self.author}\nPublication year: {self.year}\nNumber of pages: {self.pages}\nISBN: {self.isbn}\n'


#Examples of usage

book1 = Book('romain gary', 'the roots of heaven', '978-1567926262', 1956, 510)
book2 = Book('romain gary', 'promise at dawn', '978-0811210164', 1961, 374)
print(book1)
print(book2)

book3 = SelfHelpBook('dale karnegie', 'how to win friends and influence people', '1-4391-6734-6', 1936, 291)
print(book3)

book4 = FantasyNovel('william goldman', 'the princess bride', '978-0747545187', 1973, 493)
print(book4)

print(Book.search('romain gary'))
print(Book.search('the princess bride'))
print(Book.search('jSFVQJFV'))