# Library Management System

This is a simple command-line library management system built using Python and SQLAlchemy. It allows librarians to manage books and users, and members to browse, borrow, and return books.

## Features

**User Management**
     Add, view, update, and delete library users
**Book Management** 
      Add, view, update, and delete books in the library inventory
**Borrowing System**
      Track book borrowing and returns with dates
**Database Integration** 
      SQLite database with SQLAlchemy ORM

## Installation

1. **Clone the repository**:
   git clone (https://github.com/)<your_username>/<your_repo_name>.git
   cd <your_repo_name>

2. **Install dependencies**
   pipenv install

3. **Activate virtual environment**
   pipenv shell

4. **Run database migrations**
   alembic upgrade head

5. **Run the application**
   python main.py

## CLI Usage and Workflow

### Starting the Application

Run `python main.py` to start the CLI. You'll see a formatted menu with 12 numbered options.
### Menu Options and Functions
1. **Add User**
    Create a new library user with name and email:
2. **View Users**
     Display all registered users in the system
3. **Update User**
     Modify existing user information
4. **Delete User**
     Remove user and associated borrowing records
5. **Add Book** 
     Add new book to library inventory
6. **View Books**
     Display all books in library inventory
7. **Update Book** 
    Modify existing book information
8. **Delete Book** 
     Remove book and associated borrowing records
9. **Borrow Book**
     Record book borrowing transaction
10. **Return Book**
      Record book return transaction
 11. **View Borrowed Books** 
     Display all borrowing records
12. **Exit**
     close the application

## Project Structure

Library-Management-System/
├── main.py              # CLI entry point and menu system
├── helpers.py           # Business logic and CRUD operations
├── models.py            # SQLAlchemy database models
├── seed.py              # Sample data for testing
├── library.db           # SQLite database file
├── alembic.ini          # Alembic configuration
├── migrations/          # Database migration files
├── Pipfile              # Python dependencies
└── README.md            # Project documentation

## File Descriptions

### main.py
The main entry point of the application. Contains the CLI menu system and routes user choices to appropriate helper functions.

### helpers.py`
Handle logic and database operations (CRUD).
### models.py
Defines SQLAlchemy database models:
-User
-Book
-BorrowedBook

### `seed.py`
Populates the database with sample data for testing purposes.

## Database Schema

- **users**: id (PK), name (NOT NULL), email (UNIQUE, NOT NULL)
- **books**: id (PK), title (NOT NULL), author (NOT NULL), genre, copies (DEFAULT 1)
- **borrowed_books**: id (PK), user_id (FK), book_id (FK), borrow_date (NOT NULL), return_date

## Dependencies

- **SQLAlchemy**: ORM for database operations and model definitions
- **Alembic**: Database migration management and version control
- **Python 3.8+**: Runtime environment.

## License

This project is licensed under the MIT License.