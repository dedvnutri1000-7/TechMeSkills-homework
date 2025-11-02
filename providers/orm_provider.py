from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.declarative import declarative_base

from db_logic import models

import config
from providers.data_provider import data_provider

DB_URI = f'postgresql+psycopg2://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}'

engine = create_engine(DB_URI)
Base = declarative_base()


class OrmProvider(data_provider):
    session = None

    @staticmethod
    def connect():
        if OrmProvider.session:
            print('Use existing ORM provider connection')
            return OrmProvider.session
        else:
            print('Create new ORM provider connection')
            OrmProvider.session = Session(engine)
            return OrmProvider.session

    @staticmethod
    def create_tables():
        Base.metadata.create_all(engine)

    @staticmethod
    def add_author(name):
        with OrmProvider.connect() as session:
            author = models.Author(author_name=name)
            session.add(author)
            session.commit()
            return author.author_id

    @staticmethod
    def add_book(*args):
        title, publication_year, author_id = args
        with OrmProvider.connect() as session:
            book = models.Book(title=title, publication_year=publication_year, author_id=author_id)
            session.add(book)
            return book.book_id

    @staticmethod
    def add_genre(genre_name):
        with OrmProvider.connect() as session:
            genre = models.Genre(genre_name=genre_name)
            session.add(genre)
            return genre.genre_id

    @staticmethod
    def add_book_genre(book_id, genre_id):
        with OrmProvider.connect() as session:
            book_genre = models.BookGenre(book_id=book_id, genre_id=genre_id)
            session.add(book_genre)
            return book_genre.book_id, book_genre.book_genre_id

    @staticmethod
    def get_books_by_genre(genre_name):
        with OrmProvider.connect() as session:
            books = session.query(models.Book
                                  ).join(models.BookGenre
                                         ).join(models.Genre
                                                ).filter(models.Genre.genre_name.ilike(f"%{genre_name}%")).all()
            return [book.title for book in books]

    @staticmethod
    def get_books_by_author_and_year(author_name, year):
        with OrmProvider.connect() as session:
            books = session.query(models.Book).join(models.Author).filter(models.Book.publication_year == int(year)).filter(models.Author.author_name.ilike(f'%{author_name}%')).all()
            return [(book.title, book.author.author_name, book.publication_year) for book in books]
