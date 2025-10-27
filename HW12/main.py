from HW12.classes import Book, Library

library = Library()

library.add_book(Book(pages=123, year=1956, author="Толстой", price=500))
library.add_book(Book(pages=144, year=1907, author="Достоевский", price=350))
library.add_book(Book(pages=213, year=2001, author="Толстой", price=450))

print("Все книги в библиотеке:")
print(library)

print("\nИнформация о книге с ID 2:")
print(library.get_book_info(2))

print("\nПоиск по автору 'Толстой':")
for b in library.find_by_author("Толстой"):
    print(b)

print("\nПоиск по нескольким авторам ['Толстой', 'Достоевский']:")
for b in library.find_by_author(["Толстой", "Достоевский"]):
    print(b)