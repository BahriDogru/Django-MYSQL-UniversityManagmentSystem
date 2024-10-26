# Install MYsql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

# Connect to server
dataBase = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Bahri.123",
    )

# Get a cursor
cursorObject = dataBase.cursor()

# Execute a query
cursorObject.execute("CREATE DATABASE UniSystemDB")

print("Veri Tabani olusturuldu.")