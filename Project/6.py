f = open("file.txt","r")
data = f.readlines()
count = 0
for b in data:
    if b[0]=="H" and b[-3]=='d':
        count+=1
print("No of lines: ",count)
f.close()