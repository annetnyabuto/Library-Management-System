import sys
from helpers import (
    handle_add_user, list_users, handle_update_user, handle_delete_user,
    handle_add_book, list_books, handle_update_book, handle_delete_book,
    handle_borrow_book, handle_return_book, list_borrowed_books
)


def main_menu():
    print("Library Management System")
    menu_options = (
        ("1", "Add User"),
        ("2", "View Users"),
        ("3", "Update User"),
        ("4", "Delete User"),
        ("5", "Add Book"),
        ("6", "View Books"),
        ("7", "Update Book"),
        ("8", "Delete Book"),
        ("9", "Borrow Book"),
        ("10", "Return Book"),
        ("11", "View Borrowed Books"),
        ("12", "Exit")
    )
    
    for number, option in menu_options:
        print(f"{number}. {option}")
    
    choice = input("Choose an option: ")
    return choice


def myBook():
    while True:
        choice = main_menu()
        if choice == "1":
            handle_add_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            handle_update_user()
        elif choice == "4":
            handle_delete_user()
        elif choice == "5":
            handle_add_book()
        elif choice == "6":
            list_books()
        elif choice == "7":
            handle_update_book()
        elif choice == "8":
            handle_delete_book()
        elif choice == "9":
            handle_borrow_book()
        elif choice == "10":
            handle_return_book()
        elif choice == "11":
            list_borrowed_books()
        elif choice == "12":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    myBook()