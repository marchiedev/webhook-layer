import mysql.connector

dbconnection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="webhook_layer"
)