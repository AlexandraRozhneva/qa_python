import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("genre, should_be_in_children", [
        ("Фантастика", True),
        ("Мультфильмы", True),
        ("Комедии", True),
        ("Ужасы", False),
        ("Детективы", False)
    ])
    def test_get_books_for_children_by_genre(self, genre, should_be_in_children):
        collector = BooksCollector()
        collector.add_new_book("Тестовая книга")
        collector.set_book_genre("Тестовая книга", genre)
        
        children_books = collector.get_books_for_children()
        if should_be_in_children:
            assert "Тестовая книга" in children_books
        else:
            assert "Тестовая книга" not in children_books
