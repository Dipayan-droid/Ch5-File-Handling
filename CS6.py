#Code Snippet Page no 197
f = open("poem.txt","r")
str = " "
s = 0
ts = 0
while str:
    str = f.readline()
    ts = ts+len(str)
    s = s+1
print("Size of all files after removing allEOl",s)
print("The total size of all the file: ",ts)
f.close( )