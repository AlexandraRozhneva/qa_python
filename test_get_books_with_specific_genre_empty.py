import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_books_with_specific_genre_empty(self):
        collector = BooksCollector()
        result = collector.get_books_with_specific_genre("Фантастика")
        assert result == []
