from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session

Base = declarative_base()

# User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    borrowed_books = relationship("BorrowedBook", back_populates="user", cascade="all, delete-orphan")

    def __str__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"
    
    @classmethod
    def create(cls, session: Session, name, email):
        user = cls(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
    @classmethod
    def all(cls, session: Session):
        return session.query(cls).all()
    
    @staticmethod
    def update_user(session, user_id, name=None, email=None):
        user = session.query(User).get(user_id)
        if user:
            if name: user.name = name
            if email: user.email = email
            session.commit()
            print(f"User {user_id} updated!")
        return user

    @staticmethod
    def delete_user(session, user_id):
        user = session.query(User).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            print(f"User {user_id} deleted!")
        return user

# Book model
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String)
    copies = Column(Integer, default=1)
    
    borrowed_books = relationship("BorrowedBook", back_populates="book", cascade="all, delete-orphan")

    def __str__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"
    
    @classmethod
    def create(cls, session: Session, title, author, genre=None, copies=1):
        book = cls(title=title, author=author, genre=genre, copies=copies)
        session.add(book)
        session.commit()
        session.refresh(book)
        return book
    
    @classmethod
    def all(cls, session: Session):
        return session.query(cls).all()
    
    @staticmethod
    def update_book(session, book_id, title=None, author=None, genre=None, copies=None):
        book = session.query(Book).get(book_id)
        if book:
            if title: book.title = title
            if author: book.author = author
            if genre: book.genre = genre
            if copies is not None: book.copies = copies
            session.commit()
            print(f"Book {book_id} updated!")
        return book

    @staticmethod
    def delete_book(session, book_id):
        book = session.query(Book).get(book_id)
        if book:
            session.delete(book)
            session.commit()
            print(f"Book {book_id} deleted!")
        return book

# BorrowedBook model
class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    borrow_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime)
    
    user = relationship("User", back_populates="borrowed_books")
    book = relationship("Book", back_populates="borrowed_books")

    def __str__(self):
        return f"<BorrowedBook(id={self.id}, user_id={self.user_id}, book_id={self.book_id})>"
    
    @classmethod
    def create(cls, session: Session, user_id, book_id, borrow_date):
        borrowed = cls(user_id=user_id, book_id=book_id, borrow_date=borrow_date)
        session.add(borrowed)
        session.commit()
        session.refresh(borrowed)
        return borrowed
    
    @classmethod
    def all(cls, session: Session):
        return session.query(cls).all()
    
    @staticmethod
    def update_borrowed_book(session, borrowed_id, return_date=None):
        borrowed = session.query(BorrowedBook).get(borrowed_id)
        if borrowed:
            if return_date: borrowed.return_date = return_date
            session.commit()
            print(f"Borrowed book {borrowed_id} updated!")
        return borrowed

    @staticmethod
    def delete_borrowed_book(session, borrowed_id):
        borrowed = session.query(BorrowedBook).get(borrowed_id)
        if borrowed:
            session.delete(borrowed)
            session.commit()
            print(f"Borrowed book {borrowed_id} deleted!")
        return borrowed