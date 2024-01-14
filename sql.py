import sqlite3

## Connect to sqllite
connection = sqlite3.connect("student.db")

##create a cursor object to insert record,create table, retrieve
cursor = connection.cursor()

##create the table
# Creating table 
table ="""
CREATE TABLE SEMESTER(NAME VARCHAR(255), SEMESTER VARCHAR(255), 
PROGRAM VARCHAR(255));
"""

cursor.execute(table)

##insert some records

cursor.execute(''' Insert into SEMESTER values('Sumaya','2','Supply chain')''')
cursor.execute(''' Insert into SEMESTER values('Ayesha','1','Data Science')''')
cursor.execute(''' Insert into SEMESTER values('Deepa','3','AI')''')
cursor.execute(''' Insert into SEMESTER values('Rohit','2','Finance')''')

##Display all the records
print("The inserted records:")

data=cursor.execute('''Select * from SEMESTER''')

for row in data:
    print(row)

## close the connection

connection.commit()
connection.close()