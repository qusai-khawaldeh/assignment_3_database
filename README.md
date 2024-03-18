# Student_database_management
# COMP 3005


This Python script utilizes SQLAlchemy to interact with a PostgreSQL database, allowing for the creation of a student table and enabling basic CRUD (Create, Read, Update, Delete) operations..

Additionally, ensure that PostgreSQL is installed and running on your system.
1. Install pgadmin4 
2. setup postgres server, note down the port and password you will need it when setting up the connection

## Configuration
In the script, replace the following line with your actual database password:
password = '1234'  # replace with your database password
Make sure your PostgreSQL service is running and accessible.

## Usage
The script provides four main functions:

Creating the Database Table and Inserting Initial Data:
The script will automatically create a students table if it does not exist and insert some initial records.

#### getAllStudents():
Retrieves and displays all records from the students table.

#### addStudent(first_name, last_name, email, enrollment_date):
Inserts a new student record into the students table. Replace the parameters with the actual student details.

#### updateStudentEmail(student_id, new_email):
Updates the email address for a student with the specified student_id.

#### deleteStudent(student_id):
Deletes the record of the student with the specified student_id.

# Example Usage

After setting up your database connection, you can run the functions directly from your Python environment:

### Add a new student
addStudent('Ali', 'khan', 'ali.khan@example.com', '2024-03-14')

### Get all students
getAllStudents()

### Update a student's email
updateStudentEmail(1, 'new.email@example.com')

### Delete a student
deleteStudent(1)
