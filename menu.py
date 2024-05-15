


from usersg import *
from connect import connect_db, Error
from bookpish import *















def display_main_menu(connection):
    print("Welcome to the library managment system!")
    print("****")
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Quit")

def display_book_operations_menu():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

def display_user_operations_menu(connection):
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")





def main():
    connection = connect_db()
    if connection is None:
        print("Failed to connect to the database.")
        return

    try:
        while True:
            display_main_menu(connection)
            choice = input("Enter your choice: ")

            if choice == "1":
                display_book_operations_menu()
                book_choice = input("Enter your choice: ")
                if book_choice == "1":  
                    add_book(connection)

                elif book_choice == "2":  
                    borrow_book(connection)

                elif book_choice == '3':  
                    return_book(connection)

                elif book_choice == '4':  
                    search_book_by_title(connection)

                elif book_choice == '5':  
                    display_all_books(connection)

            elif choice == "2":
                display_user_operations_menu(connection)
                user_choice = input("Enter your choice: ")
                if user_choice == "1":  
                    add_new_user(connection)

                elif user_choice == "2":  
                    view_user_details(connection)

                elif user_choice == "3":  
                    display_all_users(connection)

            elif choice == "3":
               
                break
            else:
                print("Invalid choice")
    finally:
        if connection and connection.is_connected():
            connection.close()





main()





















