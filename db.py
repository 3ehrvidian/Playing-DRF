import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Password1!"
)

mycursor = mydb.cursor()

create = mycursor.execute("CREATE DATABASE drinks")
print(create)