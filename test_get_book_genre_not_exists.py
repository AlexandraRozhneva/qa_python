import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_book_genre_not_exists(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Несуществующая книга") is None
