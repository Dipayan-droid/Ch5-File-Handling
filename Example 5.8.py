#Example 5.3 
#page 210
import pickle
#dictionary objects
e1={'Empno':1201,"Name":"Anu","Age:":45,"Salary: ":47000}
e2={'Empno':1203,"Name":"Sachin","Age:":12,"Salary: ":48000}
e3={'Empno':7856,"Name":"Virat","Age:":18,"Salary: ":10}
e4 ={'Empno':4566,"Name":"Jhon","Age:":78,"Salary: ":80000}
f = open("Emp.dat","wb")
pickle.dump(e1,f)
pickle.dump(e2,f)
pickle.dump(e3,f)
pickle.dump(e4,f)
print("Successful")
f.close()