from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, User, Book, BorrowedBook
from sqlalchemy import create_engine

engine = create_engine('sqlite:///library.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Session = sessionmaker(bind=engine)

#USER HELPERS
def list_users():
    session = Session()
    users = session.query(User).all()
    for u in users:
        print(f"ID: {u.id}, Name: {u.name}, Email: {u.email}")
    session.close()

def handle_add_user():
    name = input("Enter user name: ")
    email = input("Enter user email: ")
    
    user_data = (name, email)
    
    session = Session()
    user = User(name=user_data[0], email=user_data[1])
    session.add(user)
    session.commit()
    print(f"User created: {user.name}, ID: {user.id}")
    session.close()

def handle_update_user():
    session = Session()
    list_users()
    user_id = int(input("Enter user ID to update: "))
    name = input("New name (leave blank to skip): ").strip()
    email = input("New email (leave blank to skip): ").strip()
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print("User not found!")
    else:
        if name: user.name = name
        if email: user.email = email
        session.commit()
        print(f"Updated user {user.id}: {user.name}, {user.email}")
    session.close()

def handle_delete_user():
    session = Session()
    list_users()
    user_id = int(input("Enter user ID to delete: "))
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print("User not found!")
    else:
        # Delete borrowed books first
        borrowed = session.query(BorrowedBook).filter_by(user_id=user_id).all()
        for b in borrowed:
            session.delete(b)
        session.delete(user)
        session.commit()
        print(f"Deleted user {user.id}: {user.name}")
    session.close()

#BOOK HELPERS 
def list_books():
    session = Session()
    books = session.query(Book).all()
    for b in books:
        print(f"ID: {b.id}, Title: {b.title}, Author: {b.author}, Genre: {b.genre}, Copies: {b.copies}")
    session.close()

def handle_add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    copies = int(input("Enter number of copies: "))
    session = Session()
    book = Book(title=title, author=author, genre=genre, copies=copies)
    session.add(book)
    session.commit()
    print(f"Book added: {book.title}, ID: {book.id}")
    session.close()

def handle_update_book():
    session = Session()
    list_books()
    book_id = int(input("Enter book ID to update: "))
    title = input("New title (leave blank to skip): ").strip()
    author = input("New author (leave blank to skip): ").strip()
    genre = input("New genre (leave blank to skip): ").strip()
    copies_input = input("New copies (leave blank to skip): ").strip()
    copies = int(copies_input) if copies_input else None
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        print("Book not found!")
    else:
        if title: book.title = title
        if author: book.author = author
        if genre: book.genre = genre
        if copies is not None: book.copies = copies
        session.commit()
        print(f"Updated book {book.id}: {book.title}")
    session.close()

def handle_delete_book():
    session = Session()
    list_books()
    book_id = int(input("Enter book ID to delete: "))
    book = session.query(Book).filter_by(id=book_id).first()
    if not book:
        print("Book not found!")
    else:
        # Delete borrowed records first
        borrowed = session.query(BorrowedBook).filter_by(book_id=book_id).all()
        for b in borrowed:
            session.delete(b)
        session.delete(book)
        session.commit()
        print(f"Deleted book {book.id}: {book.title}")
    session.close()

#BORROWED BOOK HELPERS
def list_borrowed_books():
    session = Session()
    borrowed = session.query(BorrowedBook).all()
    for b in borrowed:
        print(f"ID: {b.id}, User ID: {b.user_id}, Book ID: {b.book_id}, Borrow Date: {b.borrow_date}, Return Date: {b.return_date}")
    session.close()

def handle_borrow_book():
    list_users()
    user_id = int(input("Enter user ID: "))
    list_books()
    book_id = int(input("Enter book ID to borrow: "))
    borrow_date_input = input("Enter borrow date (YYYY-MM-DD) [leave blank for today]: ").strip()
    borrow_date = datetime.today() if not borrow_date_input else datetime.strptime(borrow_date_input, "%Y-%m-%d")
    session = Session()
    borrowed = BorrowedBook(user_id=user_id, book_id=book_id, borrow_date=borrow_date)
    session.add(borrowed)
    session.commit()
    print(f"Book borrowed: User {user_id}, Book {book_id}")
    session.close()

def handle_return_book():
    session = Session()
    list_borrowed_books()
    borrow_id = int(input("Enter borrowed book ID to return: "))
    borrowed = session.query(BorrowedBook).filter_by(id=borrow_id).first()
    if not borrowed:
        print("Borrowed record not found!")
    else:
        borrowed.return_date = datetime.today()
        session.commit()
        print(f"Book returned: Borrow ID {borrowed.id}")
    session.close()