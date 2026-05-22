import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_delete_book_from_favorites_not_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.delete_book_from_favorites("Несуществующая книга")
        assert len(collector.favorites) == 1
