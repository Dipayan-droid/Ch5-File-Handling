f = open("file.txt","r")
data = f.read()
count = 0
for ch in data:
    if ch.lower() in "aeiou":
        count+=1
print("No of vowels",count)