import pickle
with open("students.dat","rb") as f:
    while True:
        s = pickle.load(f)
        print(s)
f.close()