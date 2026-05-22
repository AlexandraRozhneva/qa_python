import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_set_book_genre_book_not_exists(self):
        collector = BooksCollector()
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert collector.books_genre == {}
