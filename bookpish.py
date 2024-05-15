

from connect import connect_db, Error


#theres a lot of duplicate and unnecesary code, but hey it works



def add_book(connection):
    try:
        title = input("Enter the title of the book: ")
        isbn = input("Enter the ISBN of the book: ")
        publication_date = input("Enter the publication date of the book (YYYY-MM-DD): ")

        if not title or not isbn or not publication_date:
            print("Error: Title, ISBN, and publication date are required.")
            return

        sql = "INSERT INTO books (title, isbn, publication_date) VALUES (%s, %s, %s)"
        values = (title, isbn, publication_date)

        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()

        print("Book added successfully!")
    except Error as e:
        print(f"Error: {e}")



def borrow_book(connection):
    print("Borrow a book")
    user_id = input("Enter the user ID: ")
    book_id = input("Enter the book ID: ")

    
    if not user_id.isdigit() or not book_id.isdigit():
        print(" User ID and Book ID must be numeric.")
        return

    try:
        
        cursor = connection.cursor()

        update_sql = "UPDATE books SET availability = 0 WHERE id = %s AND availability = 1" #over here we set availibilty ti zero (which means unavailable) we do this only if the id of the user_id variable that we pass in exists
        cursor.execute(update_sql, (book_id,))
        if cursor.rowcount == 0: #this counts the number of rows retrived, if its zero, then the book id doesent exist becuase it  wasnt found, so now we raise a valueerror
            raise ValueError(" Book doesent exist.")

       
        insert_sql = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, CURDATE())"
        cursor.execute(insert_sql, (user_id, book_id))

        
        connection.commit()
        print("Book borrowed successfully!")

    except Error as e:
        print(f"Error: {e}")
        
  













def return_book(connection):

   
    

    print("Return a book")
    user_id = input("Enter the user ID ")
    book_id = input("Enter the book ID ")

   
    if not user_id.isdigit() or not book_id.isdigit():
        print(" User ID and Book ID must be numeric.")
        return

    try:
       
        cursor = connection.cursor()

       
        update_book_sql = "UPDATE books SET availability = 1 WHERE id = %s" #we do the same thing as we did with the borrow book, just the opposite
        cursor.execute(update_book_sql, (book_id,))
        if cursor.rowcount == 0:
            raise ValueError(" Book not found.")

        
        update_borrowed_sql = "UPDATE borrowed_books SET return_date = CURDATE() WHERE user_id = %s AND book_id = %s AND return_date IS NULL"
        cursor.execute(update_borrowed_sql, (user_id, book_id))
        if cursor.rowcount == 0: 
            raise ValueError(" Book not borrowed by the specified user.")

        
        connection.commit()
        print("Book returned successfully!")

    except Error as e:
        print(f"Error: {e}")
        
       






def display_all_books(connection):
    try:
      
        cursor = connection.cursor()

    
        select_sql = "SELECT * FROM books"

    
        cursor.execute(select_sql)

   
        books = cursor.fetchall()

      


        for book in books:
            book_id, title, isbn, publication_date, availability = book
            print(f"{book_id}| {title}| {isbn}| {publication_date}| {'Available' if availability else 'Not Available'}")

    except Error as e:
        print(f"Error: {e}")

   




def search_book_by_title(connection):
    print("Search for a book by title")
    title = input("Enter the title of the book: ")

    try:
     
        cursor = connection.cursor()


        select_sql = "SELECT * FROM books WHERE title LIKE %s"
        
     
        cursor.execute(select_sql, ('%' + title + '%',))

  
        books = cursor.fetchall()

        if not books:
            print("No books found.")
        else:
            
           

          
            for book in books:
                book_id, title, isbn, publication_date, availability = book
                print(f"{book_id}| {title}| {isbn}| {publication_date}| {'Available' if availability else 'Not Available'}")

    except Error as e:
        print(f"Error: {e}")

  
