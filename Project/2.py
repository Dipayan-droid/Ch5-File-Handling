#2
f = open("file.txt")
data = f.read()
for ch in data:
    print(ch)
f.close()