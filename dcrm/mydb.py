import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ijaz123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All done !")
