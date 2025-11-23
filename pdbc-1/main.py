from operations import add_Employee,view_Employee,delete_Employee

print("1. add emp")
print("2. view emp")
print("3. update emp")
print("4. delete emp")
print("exit")

choose = int(input("enter option here :-- "))

if choose == 1 :
    add_Employee()
elif choose == 2 :
    view_Employee()
elif choose == 4 :
    delete_Employee()