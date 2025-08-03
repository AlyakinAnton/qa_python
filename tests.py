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

    from unittest import TestCase, main

    class TestBooksCollector(TestCase):


        def setUp(self):
            self.collector = BooksCollector()

        # Тест на добавление новых книг
        def test_add_new_book(self):
            self.collector.add_new_book('Книга1')
            self.collector.add_new_book('Книга2')
            self.assertEqual(len(self.collector.get_books_genre()), 2)
            self.collector.add_new_book('Книга1')
            self.assertEqual(len(self.collector.get_books_genre()), 2)
            long_title = 'a' * 41
            self.collector.add_new_book(long_title)
            self.assertNotIn(long_title, self.collector.get_books_genre())

        # Тест установки жанра книги
        def test_set_book_genre(self):
            self.collector.add_new_book('Ромео и Джульетта')
            self.collector.set_book_genre('Ромео и Джульетта', 'Фантастика')
            genre = self.collector.get_book_genre('Ромео и Джульетта')
            self.assertEqual(genre, 'Фантастика')
            unavailable_genre = 'Научпоп'
            self.collector.set_book_genre('Ромео и Джульетта', unavailable_genre)
            genre_after_invalid_change = self.collector.get_book_genre('Ромео и Джульетта')
            self.assertNotEqual(genre_after_invalid_change, unavailable_genre)

        # Тест получения жанра книги
        def test_get_book_genre(self):
            self.collector.add_new_book('Сказка')
            self.collector.set_book_genre('Сказка', 'Мультфильмы')
            genre = self.collector.get_book_genre('Сказка')
            self.assertEqual(genre, 'Мультфильмы')

        # Тест выбора книг конкретного жанра.
        def test_get_books_with_specific_genre(self):
            self.collector.add_new_book('Шерлок Холмс')
            self.collector.set_book_genre('Шерлок Холмс', 'Детективы')
            self.collector.add_new_book('Хоббит')
            self.collector.set_book_genre('Хоббит', 'Фантастика')
            fantasy_books = self.collector.get_books_with_specific_genre('Фантастика')
            detective_books = self.collector.get_books_with_specific_genre('Детективы')
            self.assertListEqual(fantasy_books, ['Хоббит'])
            self.assertListEqual(detective_books, ['Шерлок Холмс'])

        # Тест получения словаря книг
        def test_get_books_genre(self):
            self.collector.add_new_book('Анна Каренина')
            self.collector.set_book_genre('Анна Каренина', 'Фантастика')
            current_state = self.collector.get_books_genre()
            expected_result = {'Анна Каренина': 'Фантастика'}
            self.assertDictEqual(current_state, expected_result)

        # Тест получения книг для детей
        def test_get_books_for_children(self):
            self.collector.add_new_book('Том и Джерри')
            self.collector.set_book_genre('Том и Джерри', 'Мультфильмы')
            children_books = self.collector.get_books_for_children()
            self.assertListEqual(children_books, ['Том и Джерри'])

        # Тест добавления книги в избранное
        def test_add_book_in_favorites(self):
            self.collector.add_new_book('Гарри Поттер')
            self.collector.add_book_in_favorites('Гарри Поттер')
            favorite_books = self.collector.get_list_of_favorites_books()
            self.assertListEqual(favorite_books, ['Гарри Поттер'])
            self.collector.add_book_in_favorites('Гарри Поттер')
            self.assertListEqual(favorite_books, ['Гарри Поттер'])

        # Тест удаления книги из избранного
        def test_delete_book_from_favorites(self):
            self.collector.add_new_book('Матрица')
            self.collector.add_book_in_favorites('Матрица')
            self.collector.delete_book_from_favorites('Матрица')
            favorite_books = self.collector.get_list_of_favorites_books()
            self.assertFalse(favorite_books)

        # Тест получения списка избранных книг
        def test_get_list_of_favorites_books(self):
            self.collector.add_new_book('Пиноккио')
            self.collector.add_book_in_favorites('Пиноккио')
            favorite_books = self.collector.get_list_of_favorites_books()
            self.assertListEqual(favorite_books, ['Пиноккио'])

    if __name__ == '__main__':
        main()