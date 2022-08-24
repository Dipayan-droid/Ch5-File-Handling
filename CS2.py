#Code Snippet 2 Pg 194
myfile = open("poem.txt","r")
str = myfile.read(30)
print(str)
str2 = myfile.read(50)
print(str2)
str3 = myfile.read()
myfile.close()
print (str3)