import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_books_for_children_skip_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга без жанра")
        
        children_books = collector.get_books_for_children()
        assert "Книга без жанра" not in children_books
