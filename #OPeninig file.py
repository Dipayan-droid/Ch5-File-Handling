#OPeninig gfile
import pickle
f = open("students.dat","rb")
s = ""
try:
    while True:
        s = pickle.load(f)
        print(s)
except EOFError:
    f.close()