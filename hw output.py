import csv
f = open("employee.csv","r")
rd = csv.reader(f)
for r in rd:
    print(r)