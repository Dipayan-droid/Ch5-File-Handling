f = open("file.txt","r")
data = f.read()
count = 0
a = f.readlines()
for ch in a:
    if len(ch.split())>=4:
        count+=1
print("No of lines:",count)
f.close()