import sqlite3
import os

sqliteConnection = sqlite3.connect(os.path.expanduser('~/Desktop/Python/currentProjects/projectTest/db/test1.db'))

crsr = sqliteConnection.cursor()

## next till ## taken from https://www.geeksforgeeks.org/sql-using-python/ 

# primary key
pk = [2, 3, 4, 5, 6]
 
# Enter 5 students first names
f_name = ['Nikhil', 'Nisha', 'Abhinav', 'Raju', 'Anshul']
 
# Enter 5 students last names
l_name = ['Aggarwal', 'Rawat', 'Tomar', 'Kumar', 'Aggarwal']
 
# Enter their gender respectively
gender = ['M', 'F', 'M', 'M', 'F']
 
# Enter their joining data respectively
date = ['2019-08-24', '2020-01-01', '2018-05-14', '2015-02-02', '2018-05-14']
 
for i in range(5):
 
    # This is the q-mark style:
    crsr.execute(f'INSERT INTO emp VALUES ({pk[i]}, "{f_name[i]}", "{l_name[i]}", "{gender[i]}", "{date[i]}")')
 
# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
sqliteConnection.commit()

##



sqliteConnection.close()

print('success')