import sqlite3
import os
 
# connecting to the database
sqliteConnection = sqlite3.connect(os.path.expanduser('~/Desktop/Python/currentProjects/projectTest/db/test1.db'))

crsr = sqliteConnection.cursor()
 
# SQL command to create a table in the database
sql_command = """CREATE TABLE emp (
staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR(1),
joining DATE);"""
 
# execute the statement
crsr.execute(sql_command)
 
# close the connection
sqliteConnection.close()