import sqlite3

## Connect to sqlite3
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table and retrieve
cursor = connection.cursor()

## Create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

## Insert some records
cursor.execute('''Insert Into STUDENT values('Pradeep', 'Data Science', 'A', 90)''')
cursor.execute('''Insert Into STUDENT values('Prameela', 'Data Science', 'B', 100)''')
cursor.execute('''Insert Into STUDENT values('Anish', 'Data Science', 'A', 95)''')
cursor.execute('''Insert Into STUDENT values('Deepak', 'Dev Ops', 'A', 86)''')
cursor.execute('''Insert Into STUDENT values('Bhargav', 'Dev Ops', 'B', 93)''')

## Display all the records
print("The inserted records are")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(data)

## Close the connection
connection.commit()
connection.close()