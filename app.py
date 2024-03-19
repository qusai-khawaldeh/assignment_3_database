# Importing necessary libraries
import pandas as pd
from sqlalchemy import create_engine, text

def create_database_and_table(username,port,db_name):
    """Function to create the database and students table."""
    password = '1234'  # replace with your actual database password
    engine = create_engine(f"postgresql://{username}:{password}@localhost:{port}")
    conn = engine.connect()
    conn.execute("COMMIT")
    try:
        conn.execute(f"CREATE DATABASE {db_name}")
        print("Database created successfully!")
        # Now connect to the newly created database and create the students table
        engine = create_engine(f"postgresql://{username}:{password}@localhost:{port}/{db_name}")
        conn1 = engine.connect()
        conn1.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date DATE
            )
            """)
        conn1.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
        """)
        print("Table 'students' created and initial data inserted.")
        conn1.close()
    except:
        print("Database already exists.")
    finally:
        conn.close()
        

        
def connect_to_db(username,port,db_name):
    """Function to connect to the database"""
    password = '1234'  # replace with your actual database password
    engine = create_engine(f"postgresql://{username}:{password}@localhost:{port}/{db_name}")
    return engine.connect()

def getAllStudents(conn):
    """ Function definitions for CRUD operations"""
    student_details = pd.read_sql_query("SELECT * FROM students", con=conn)
    print(student_details)

def addStudent(conn, first_name, last_name, email, enrollment_date):
    """"Function to add data into table"""
    insert_query = text("""
        INSERT INTO students (first_name, last_name, email, enrollment_date) 
        VALUES (:first_name, :last_name, :email, :enrollment_date)
    """)
    conn.execute(insert_query, {'first_name': first_name, 'last_name': last_name, 'email': email, 'enrollment_date': enrollment_date})

def updateStudentEmail(conn, student_id, new_email):
    """"Function to update student email"""
    update_query = text("""
        UPDATE students 
        SET email = :email 
        WHERE student_id = :student_id
    """)
    conn.execute(update_query, {'email': new_email, 'student_id': student_id})

def deleteStudent(conn, student_id):
    """"Function to delete  student email"""
    delete_query = text("DELETE FROM students WHERE student_id = :student_id")
    conn.execute(delete_query, {'student_id': student_id})

def main():
    db_name = input("Enter the name of the database to use: ")
    db_user = input("Enter the your username:")
    db_port =  input("Enter the your port:")
    create_database_and_table(db_user,db_port,db_name)  # Create DB and table using the user-specified name
    conn = None
    try:
        conn = connect_to_db(db_user,db_port,db_name)  # Connect to the database
        while True:  # Main application loop
            print("\n1. View all students\n2. Add a new student\n3. Update a student's email\n4. Delete a student\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                getAllStudents(conn)
            elif choice == '2':
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
                addStudent(conn, first_name, last_name, email, enrollment_date)
            elif choice == '3':
                student_id = int(input("Enter student ID to update: "))
                new_email = input("Enter new email: ")
                updateStudentEmail(conn, student_id, new_email)
            elif choice == '4':
                student_id = int(input("Enter student ID to delete: "))
                deleteStudent(conn, student_id)
            elif choice == '5':
                break  # Exit the application
            else:
                print("Invalid choice, please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()