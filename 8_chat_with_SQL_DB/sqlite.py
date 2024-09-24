import sqlite3

# conect with sqlite
db = sqlite3.connect("student.db")

# create cursor
cursor = db.cursor()

# Create the table
table_info = """
create table STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
    )
"""

cursor.execute(table_info)

# insert data
insert_info = """
insert into STUDENT
values
    ('Rohit', 'Data Science', 'A', 100),
    ('Krish', 'Data Science', 'A', 90),
    ('John', 'Devops', 'B', 100),
    ('Mukesh', 'Data Science', 'A', 86),
    ('Jacob', 'Devops', 'A', 50),
    ('Dipesh', 'Web Development', 'A', 35)
"""

cursor.execute(insert_info)

# Display all the records
print("The inserted records are")
data = cursor.execute("Select * from STUDENT")
for row in data:
    print(row)

db.commit()
db.close()
print("Database closed")