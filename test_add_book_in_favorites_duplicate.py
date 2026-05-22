import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        assert collector.favorites.count("Война и мир") == 1
