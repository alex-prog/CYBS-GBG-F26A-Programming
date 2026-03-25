# This file is using the mysql-connector-python package, which can be installed using pip:
# pip install mysql-connector-python
# or
# pip3 install mysql-connector-python
# or
# python -m pip install mysql-connector-python
import mysql.connector

# the following variables should be filled with the appropriate values for your MySQL database
# you can find the host, user, password, and database in the slide deck of the lecture
host = ""
user = ""
password = ""
database = ""

conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
c = conn.cursor()
c.execute("SELECT * FROM students")
data = c.fetchall()
if not len(data):
    print("Table is empty!")
else:
    print(data)
