-- Library Project SQL

CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author_id INTEGER,
    publication_year INTEGER,
    FOREIGN KEY(author_id) REFERENCES authors(id)
);

CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(book_id) REFERENCES books(id)
);

INSERT INTO authors (first_name, last_name) VALUES
('George', 'Orwell'),
('J.K.', 'Rowling'),
('Leo', 'Tolstoy');

INSERT INTO books (title, author_id, publication_year) VALUES
('1984', 1, 1949),
('Animal Farm', 1, 1945),
('Harry Potter', 2, 1997),
('War and Peace', 3, 1869),
('Book With No Author', NULL, 2000);

INSERT INTO sales (book_id, quantity) VALUES
(1, 120),
(2, 80),
(3, 200),
(4, 50);
