import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_new_book("Преступление и наказание")
        collector.set_book_genre("Война и мир", "Детективы")
        collector.set_book_genre("Преступление и наказание", "Детективы")
        
        result = collector.get_books_with_specific_genre("Детективы")
        assert len(result) == 2
        assert "Война и мир" in result
        assert "Преступление и наказание" in result
