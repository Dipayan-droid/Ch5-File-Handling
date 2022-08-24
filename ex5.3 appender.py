#ex5.3 append
f = open("Marks.txt","a")
c = int(input("Enter the no of stdents: "))
for i in range(c):
    print("Enter the data of ",i+1,"student: " )
    r = int(input("Enter roll : "))
    n = input("Enter name: ")
    m = float(input("Enter marks: "))
    rec = str(r)+","+n+","+str(m)+"\n"
    f.write(rec)
f.close()