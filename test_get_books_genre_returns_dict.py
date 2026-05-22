import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        
        result = collector.get_books_genre()
        assert isinstance(result, dict)
        assert result == collector.books_genre
