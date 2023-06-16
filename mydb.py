import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1866"

)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Create database
cursorObject.execute("CREATE DATABASE kwabsdb")

print("All Done!")
