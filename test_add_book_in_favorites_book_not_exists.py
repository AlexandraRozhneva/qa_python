import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_book_in_favorites_book_not_exists(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Несуществующая книга")
        assert collector.favorites == []
