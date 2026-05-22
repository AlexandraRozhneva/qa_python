from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("name", ["", "a" * 41, "a" * 100])
    def test_add_new_book_invalid_name_length(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre
