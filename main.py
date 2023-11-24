from client import Client
from prettytable import PrettyTable

if __name__ == "__main__":
    client = Client("localhost", "Assignment4", "postgres", "password", 5432)
    while 1:
        print("""\nAssignment 4
              
              Please select an option
              [1] Get all students
              [2] Add student
              [3] Update student email
              [4] Delete student

              """)
        choice = input(">>> ")
        if choice == '1':
            # Get students tuple from client and print to table
            students = client.getAllStudents()
            table = PrettyTable()
            table.field_names = ["Student ID", "First Name", "Last Name", "Email", "Enrollment Date"]
            table.add_rows(students)
            print(table)
        elif choice == '2':
            # Prompt user for student info then send to addStudent method in client
            first_name, last_name, email, enrollment_date = input("Enter student information: ").split(',')
            result, msg = client.addStudent(first_name, last_name, email, enrollment_date)
            print(msg)
        elif choice == '3':
            # Prompt the user for the student id and new email then send to updateStudentEmail method in client
            student_id = input("Enter student id: ")
            email = input("Enter new email: ")
            result, msg = client.updateStudentEmail(student_id, email)
            print(msg)
        elif choice == '4':
            # Prompt the user for the student id and then send to deleteStudent method in client
            student_id = input("Enter student id: ")
            result, msg = client.deleteStudent(student_id)
            print(msg)
        else:
            print("Invalid choice")