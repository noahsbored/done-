import mysql.connector
from mysql.connector import Error


def add_new_user(connection):
    print("add a new user")
    name = input("enter the name of the user: ")
    email = input("enter the email of the user: ")

    try:
                                       #we add users by  name and we make sure the email isint alredy being used
        cursor = connection.cursor()

        select_sql = "SELECT * FROM users WHERE email = %s"
        cursor.execute(select_sql, (email,))
        existing_user = cursor.fetchone() #fetchone takes all the values in the row i selected so in the case of email, it will have all the values of the row where email is located
        if existing_user:
            print(" user with this email already exists") 
            return

       
        insert_sql = "INSERT INTO users (name, email) VALUES (%s, %s)" #we use parameters the argument we accept is the input we passed in that the user types
        cursor.execute(insert_sql, (name, email))                        
        connection.commit()
        
        print("user added successfully!")

    except Error as e:
        print(f"Error: {e}")
       

  













def view_user_details(connection):
    print("View user details")
    user_id = input("Enter the user ID: ")

    try:
        
        cursor = connection.cursor()

    
        select_sql = "SELECT * FROM users WHERE id = %s"

   
        cursor.execute(select_sql, (user_id,))

       
        user = cursor.fetchone()        

        if user:
            print( user[0])  
            print( user[1])
            print( user[2])
        else:
            print("user not found.")

    except Error as e:
        print(f"Error: {e}")
















def display_all_users(connection):
    try:
        
        cursor = connection.cursor()

     
        select_sql = "SELECT * FROM users"

       
        cursor.execute(select_sql)

     
        users = cursor.fetchall()

        if not users:
            print("No users found.")
        else:
            
           
         

        
            for user in users:
                user_id, name, email = user
                print(f"{user_id}| {name}| {email}")

    except Error as e:
        print(f"Error: {e}")

 