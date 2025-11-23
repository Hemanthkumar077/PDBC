from db import get_connection 
# it imported from db.py file because
# we create only conncection to the db but we didn't use the db 
# so we have to import db to use that conncetion to insert or send values to db 
def add_Employee():
    connectionToDB = get_connection() # we compulsory call connection otherwise it did not execute 
    emp_name = input("enter employee name :-- ")
    emp_sal = float(input("enter salary :-- "))
    emp_dept = input("enter employee dept :-- ")
    emp_loc = input("enter employee location :-- ")
    cur = connectionToDB.cursor() # cursor is an function to communicate with the db from the py file
    cur.execute("insert into Employes(emp_name , emp_sal , emp_dept , emp_loc) values (%s ,%s ,%s,%s) ", (emp_name , emp_sal , emp_dept , emp_loc))
    # execute is used to execute given input from py file to db
    connectionToDB.commit()
    connectionToDB.close()
    print(f"{emp_name} employee added successfully")
    
def view_Employee():
    connectionToDB  = get_connection()
    cur = connectionToDB.cursor()
    cur.execute( "select * from Employes")
    data = cur.fetchall()
    print(data)
    connectionToDB.close()  
    
def delete_Employee():
    connectionToDB = get_connection()
    cur = connectionToDB.cursor()
    emp_id = int(input("enter delete emp_id :-- "))
    cur.execute("delete from Employes where emp_id = (%s)",(emp_id,))
    connectionToDB.commit()
    connectionToDB.close()
    print(f"delete {emp_id} sucessfully ")
    
    