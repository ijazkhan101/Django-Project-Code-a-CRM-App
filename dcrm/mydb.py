import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # hostname
    user="root",                   # the user who has privilege to the db
    passwd="ijaz123",  # password for user
    database="Factdb",  # database name
    auth_plugin='mysql_native_password',

)

cursorObject = mydb.cursor()

cursorObject.execute("CREATE DATABASE Factdb")

print("All done !")
