import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_list_of_favorites_books_with_books(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_new_book("Преступление и наказание")
        collector.add_book_in_favorites("Война и мир")
        collector.add_book_in_favorites("Преступление и наказание")
        
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert "Война и мир" in favorites
        assert "Преступление и наказание" in favorites
