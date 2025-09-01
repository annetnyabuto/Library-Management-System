from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Book
from datetime import datetime

engine = create_engine('sqlite:///library.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(engine)

def seed_data():
    session = SessionLocal()
    
    # Add sample users
    users = [
        User(name="Alice Johnson", email="alice@email.com"),
        User(name="Bob Smith", email="bob@email.com"),
        User(name="Carol Davis", email="carol@email.com")
    ]
    
    # Add sample books
    books = [
        Book(title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction", copies=3),
        Book(title="1984", author="George Orwell", genre="Dystopian", copies=2),
        Book(title="Pride and Prejudice", author="Jane Austen", genre="Romance", copies=2),
        Book(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction", copies=1)
    ]
    
    session.add_all(users + books)
    session.commit()
    session.close()
    print("Sample data added successfully!")

if __name__ == '__main__':
    seed_data()