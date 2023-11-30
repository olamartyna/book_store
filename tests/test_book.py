from lib.book import Book

"""
Book constructs with an id, title and author name
"""
def test_book_constructs():
    book = Book(1, "Test Title", "Test Author")
    assert book.id == 1
    assert book.title == "Test Title"
    assert book.author_name == "Test Author"

"""
Books nicely formatted to strings
That's thanls to __repr__ method
"""
def test_book_format_nicely():
    book = Book(1, "Test Title", "Test Author")
    assert str(book) == "Book(1, Test Title, Test Author)"

"""
When we compare two identical books, we want them to be equal
That's thanks to __eq__ method
"""
def test_books_are_equal():
    book1 = Book(1, "Test Title", "Test Author")
    book2 = Book(1, "Test Title", "Test Author")
    assert book1 == book2

