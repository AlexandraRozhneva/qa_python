from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre
        assert collector.books_genre["Война и мир"] == ""
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_new_book("Война и мир")
        assert len(collector.books_genre) == 1
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("name", ["", "a" * 41, "a" * 100])
    def test_add_new_book_invalid_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        assert collector.books_genre["Война и мир"] == "Фантастика"
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_set_book_genre_book_not_exists(self):
        collector = BooksCollector()
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert collector.books_genre == {}
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Несуществующий жанр")
        assert collector.books_genre["Война и мир"] == ""
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_book_genre_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Детективы")
        assert collector.get_book_genre("Война и мир") == "Детективы"
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_book_genre_not_exists(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Несуществующая книга") is None
    
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
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_books_with_specific_genre_empty(self):
        collector = BooksCollector()
        result = collector.get_books_with_specific_genre("Фантастика")
        assert result == []
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        
        result = collector.get_books_with_specific_genre("Несуществующий жанр")
        assert result == []
    
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
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_books_for_children_skip_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга без жанра")
        
        children_books = collector.get_books_for_children()
        assert "Книга без жанра" not in children_books
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        assert "Война и мир" in collector.favorites
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        assert collector.favorites.count("Война и мир") == 1
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_book_in_favorites_book_not_exists(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Несуществующая книга")
        assert collector.favorites == []
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.delete_book_from_favorites("Война и мир")
        assert "Война и мир" not in collector.favorites
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_delete_book_from_favorites_not_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.delete_book_from_favorites("Несуществующая книга")
        assert len(collector.favorites) == 1
    
import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
    
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
