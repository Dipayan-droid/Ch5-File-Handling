#School hw
import csv
f = open("employee.csv","a")
name = input("Enter the name of the employee: ")
no = input("Enter employee number: ")
s = input("Enter the salary: ")
emp = (name,no,s)
wr = csv.writer(f)
wr.writerow(emp)
f.close()