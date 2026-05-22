import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        
        result = collector.get_books_with_specific_genre("Несуществующий жанр")
        assert result == []
