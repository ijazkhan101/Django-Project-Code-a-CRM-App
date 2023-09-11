import mysql.connector

dataBase = mysql.connector.connect(
    host = 'loclhost',
    user = 'root',
    password ='Bismakhan101'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All done !")