# Student_database_management
# COMP 3005

This Python script utilizes SQLAlchemy to interact with a PostgreSQL database, allowing for the creation of a student table and enabling basic CRUD (Create, Read, Update, Delete) operations..

### Prerequisites
Before running this script, make sure that PostgreSQL is installed and running on your system. Follow these steps:
1. Install PgAdmin 4.
2. pip install sqlalchemy
3. Set up the PostgreSQL server, noting down the port and password as you will need these details to set up the database connection in the script.
4. Ensure PgAdmin is running before you excute the script.
   
## Configuration
In the script, replace the following line with your actual database password:
password = '1234'  # replace with your database password
Make sure your PostgreSQL service is running and accessible.

## Usage
The script provides four main functions:

Creating the Database Table and Inserting Initial Data:
The script will automatically create a students table if it does not exist and insert some initial records.
```plaintext
CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date DATE
            )
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
```
#### getAllStudents():
Retrieves and displays all records from the students table.

#### addStudent(first_name, last_name, email, enrollment_date):
Inserts a new student record into the students table. Replace the parameters with the actual student details.

#### updateStudentEmail(student_id, new_email):
Updates the email address for a student with the specified student_id.

#### deleteStudent(student_id):
Deletes the record of the student with the specified student_id.

# Example Usage

After setting up your database connection, you can run the functions directly from your terminal by 

python app.py 

## Application Interaction

Once the application is running, you will be presented with a menu of options for managing the student database:

```plaintext
1. View all students
2. Add a new student
3. Update a student's email
4. Delete a student
5. Exit 
```
### Get all students
option 1: View All students will execute the following function:
getAllStudents()

### Add a new student
option 2: Will allow you to add student into the students table
addStudent('Ali', 'khan', 'ali.khan@example.com', '2024-03-14')

### Update a student's email
option 3: Will allow you to update a students email
updateStudentEmail(1, 'new.email@example.com')

### Delete a student
option 4: Will allow you to delete a student record
deleteStudent(1)

### End script
option 5: will end the script.
