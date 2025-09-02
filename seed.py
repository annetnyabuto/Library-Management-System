from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Book
from datetime import datetime

engine = create_engine('sqlite:///library.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def seed_data():
    session = SessionLocal()
    user_data = (
        ("Alice Johnson", "alice@email.com"),
        ("Bob Smith", "bob@email.com"),
        ("Carol Davis", "carol@email.com")
    )
    
    users = []
    for name, email in user_data:
        users.append(User(name=name, email=email))
    
    book_data = (
        ("To Kill a Mockingbird", "Harper Lee", "Fiction", 3),
        ("1984", "George Orwell", "Dystopian", 2),
        ("Pride and Prejudice", "Jane Austen", "Romance", 2),
        ("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1)
    )
    
    books = []
    for title, author, genre, copies in book_data:
        books.append(Book(title=title, author=author, genre=genre, copies=copies))
    
    session.add_all(users + books)
    session.commit()
    session.close()
    print("Sample data added successfully!")

if __name__ == '__main__':
    seed_data()