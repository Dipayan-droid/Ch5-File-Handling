#ex5.3 opener
f = open("Marks.txt","r")
while str:
    str = f.readline()
    print(str)
f.close()