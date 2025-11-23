import mysql.connector # this is the connector to connect db and py files

def get_connection():  # we need to return db conncetion to the other file to use the conncetion ( that's why we place conncetor in an function)
    return mysql.connector.connect( # these are the db details 
    host = "localhost",
    user = "root",
    password = "Hemanth9392",
    database = "EmployeManagementSystem"
)

print("db connected successfully")