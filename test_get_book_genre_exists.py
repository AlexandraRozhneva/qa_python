import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_book_genre_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Детективы")
        assert collector.get_book_genre("Война и мир") == "Детективы"
