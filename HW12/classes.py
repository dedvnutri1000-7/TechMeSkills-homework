'''
ДЗ
Библиотека:
- Класс Book:
   Используем dataclass для создания книги.
   Атрибуты: book_id, pages, year, author, price. Book_id по умолчанию None присваивается только при добавлении книги в библиотеку.
   Выполняем валидацию атрибутов при создании книги. Для валидации создаем собственные исключения
   Реализуем метод сравнения книг по цене.

- Класс Library:
   Хранит книги и автоматически присваивает каждой книге уникальный id.
   Имеет методы add_book и get_book_info.
   Поддерживает метод для поиска книг по автору с перегрузкой: можно искать по одному автору или передавать список авторов.

Переопределить методы str в классах для красивого вывода объектов

Примечание: в рамках задание создать два файла: classes.py и main.py.
В первом будут описаны все классы, во втором классы будут импортированы и
использованы.
'''


from dataclasses import dataclass
@dataclass
class Book:
    pages: int
    year: int
    author: str
    price: float
    book_id: int = None

    def __post_init__(self):
        if self.pages <= 0:
            raise ValueError("Количество страниц должно быть позитивным")
        if self.year <= 0:
            raise ValueError("Год должен быть положительным")
        if self.author == '':
            raise ValueError("Автор не может быть пустым")

class Library:
    def __init__(self):
        self.books = []
        self._next_id = 1

    def add_book(self, book: Book):
        book.book_id = self._next_id
        self._next_id += 1
        self.books.append(book)

    def get_book_info(self, book_id: int):
        for book in self.books:
            if book.book_id == book_id:
                return str(book)
        return "Книга не найдена"

    def find_by_author(self, author):
        result = []

        if isinstance(author, str):
            for book in self.books:
                if book.author == author:
                    result.append(book)

        elif isinstance(author, list):
            for book in self.books:
                if book.author in author:
                    result.append(book)

        return result

    def __str__(self):
        result = ""
        for book in self.books:
            result += str(book) + "\n"
        return result.strip()

