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


from unittest import TestCase
from myapp.books_collector import BooksCollector


class TestBooksCollector(TestCase):

    def setUp(self):
        self.collector = BooksCollector()

    # Тест на добавление новой книги
    def test_add_new_book(self):
        self.assertEqual(len(self.collector.get_books_genre()), 0)
        self.collector.add_new_book('Книга1')
        self.assertEqual(len(self.collector.get_books_genre()), 1)

    # Тест на установку жанра книги
    def test_set_book_genre(self):
        self.collector.add_new_book('Ромео и Джульетта')
        self.collector.set_book_genre('Ромео и Джульетта', 'Фантастика')
        genre = self.collector.get_book_genre('Ромео и Джульетта')
        self.assertEqual(genre, 'Фантастика')

    # Тест на получение жанра книги
    def test_get_book_genre(self):
        self.collector.add_new_book('Ромео и Джульетта')
        self.collector.set_book_genre('Ромео и Джульетта', 'Фантастика')
        direct_access = self.collector.books_genre['Ромео и Джульетта']
        method_access = self.collector.get_book_genre('Ромео и Джульетта')
        self.assertEqual(direct_access, method_access)

    # Тест на получение книг конкретного жанра
    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book('Шерлок Холмс')
        self.collector.set_book_genre('Шерлок Холмс', 'Детективы')
        self.collector.add_new_book('Хоббит')
        self.collector.set_book_genre('Хоббит', 'Фантастика')
        fantasy_books = self.collector.get_books_with_specific_genre('Фантастика')
        self.assertListEqual(fantasy_books, ['Хоббит'])

    # Тест на получение словаря книг
    def test_get_books_genre(self):
        self.collector.add_new_book('Анна Каренина')
        self.collector.set_book_genre('Анна Каренина', 'Фантастика')
        current_state = self.collector.get_books_genre()
        expected_result = {'Анна Каренина': 'Фантастика'}
        self.assertDictEqual(current_state, expected_result)

    # Тест на получение детских книг
    def test_get_books_for_children(self):
        self.collector.add_new_book('Том и Джерри')
        self.collector.set_book_genre('Том и Джерри', 'Мультфильмы')
        self.collector.add_new_book('Секрет фирмы')
        self.collector.set_book_genre('Секрет фирмы', 'Детективы')
        children_books = self.collector.get_books_for_children()
        self.assertListEqual(children_books, ['Том и Джерри'])

    # Тест на добавление книги в избранное
    def test_add_book_in_favorites(self):
        self.collector.add_new_book('Гарри Поттер')
        self.collector.add_book_in_favorites('Гарри Поттер')
        favorite_books = self.collector.get_list_of_favorites_books()
        self.assertListEqual(favorite_books, ['Гарри Поттер'])

    # Тест на удаление книги из избранного
    def test_delete_book_from_favorites(self):
        self.collector.add_new_book('Матрица')
        self.collector.add_book_in_favorites('Матрица')
        self.collector.delete_book_from_favorites('Матрица')
        favorite_books = self.collector.get_list_of_favorites_books()
        self.assertListEqual(favorite_books, [])

    # Тест на получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        self.collector.add_new_book('Пиноккио')
        self.collector.add_book_in_favorites('Пиноккио')
        favorite_books = self.collector.get_list_of_favorites_books()
        self.assertListEqual(favorite_books, ['Пиноккио'])


if __name__ == '__main__':
    import unittest

    unittest.main()