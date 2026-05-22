import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
