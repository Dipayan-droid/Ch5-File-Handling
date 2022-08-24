f = open("file.txt","r")
count = 0
data = f.readlines()
for ch in data:
    if ch[0]=='h' or ch[0]=='H':
        count+=1
print("No of lines:",count)
f.close()