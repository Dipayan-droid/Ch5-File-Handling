#School programming Practice 1 
import pickle
f = open("students.dat","wb")
n = input("Enter the name of the student: ")
c = input("Enter the class of the student: ")
s = input("Enter the section of the student: ")
r = int(input("Enter the roll number of the student: "))
stud_info = [n,c,s,r]
pickle.dump(stud_info,f)
f.close()