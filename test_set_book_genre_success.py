import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        assert collector.books_genre["Война и мир"] == "Фантастика"
