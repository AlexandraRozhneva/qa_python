import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Несуществующий жанр")
        assert collector.books_genre["Война и мир"] == ""
