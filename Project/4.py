f = open("File.txt","r")
data = f.read()
count = 0
for ch in data:
    if ch.isspace()==True:
        count+=1
print("No of spaces:",count)
f.close()
