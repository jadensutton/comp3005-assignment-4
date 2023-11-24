import psycopg2

class Client:
    def __init__(self, host: str, dbname: str, user: str, password: str, port: int):
        self._host = host
        self._dbname = dbname
        self._user = user
        self._password = password
        self._port = port

    def _connect(self):
        # Return a new postgres connection
        return psycopg2.connect(host=self._host, dbname=self._dbname, user=self._user, password=self._password, port=self._port)

    def getAllStudents(self) -> list[tuple]:
        connection = self._connect()
        cursor = connection.cursor()

        # Execute select query, fetch the result from cursor then return
        cursor.execute("""SELECT * FROM students
                       """)
        
        students = cursor.fetchall()
        
        connection.commit()
        cursor.close()
        connection.close()

        return students

    def addStudent(self, first_name: str, last_name: str, email: str, enrollment_date: str) -> tuple[int, str]:
        connection = self._connect()
        cursor = connection.cursor()

        #Insert new student into table
        try:
            cursor.execute(f"""INSERT INTO students (first_name, last_name, email, enrollment_date)
                        VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');
                        """)
        except psycopg2.errors.UniqueViolation:
            # Email is not unique
            return (1, "Email must be unique")
        
        connection.commit()
        cursor.close()
        connection.close()

        return (0, "Success")

    def updateStudentEmail(self, student_id: int, new_email: str) -> tuple[int, str]:
        connection = self._connect()
        cursor = connection.cursor()

        # Update the email of the student with matching id
        try:
            cursor.execute(f"""UPDATE students
                            SET email = '{new_email}'
                            WHERE student_id = {student_id} 
                        """)
        except psycopg2.errors.UniqueViolation:
            return (1, "Email must be unique")
            
        
        connection.commit()
        cursor.close()
        connection.close()

        return (0, "Success")
    
    def deleteStudent(self, student_id: int) -> tuple[int, str]:
        connection = self._connect()
        cursor = connection.cursor()

        #Delete student with matching id
        cursor.execute(f"""DELETE FROM students
                        WHERE student_id = {student_id} 
                       """)
        
        connection.commit()
        cursor.close()
        connection.close()

        return (0, "Success")
