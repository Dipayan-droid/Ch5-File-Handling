import csv
f = open("students.csv","r")
rd = csv.reader(f)
for r in rd:
    print(r)