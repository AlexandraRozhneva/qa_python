from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre
        assert collector.books_genre["Война и мир"] == ""
