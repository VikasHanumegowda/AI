import os
from Assignment2 import homework3
count = 0
while True:
    count += 1
    execute = input()
    os.system("python homework3.py")
    f = open("inp.txt", "r")
    n = int(f.readline().strip())
    p = int(f.readline().strip())
    t = float(f.readline().strip())
    f.close()
    f = open("inp.txt", "w")
    f.write(str(n) + "\n")
    f.write(str(p) + "\n")
    f.write(str(t) + "\n")
    out = open("output.txt", "r")
    firstline = out.readline()
    for x in range(n):
        temp = out.readline()
        print(temp)
        f.write(temp)
    f.close()
    out.close()

    print("done" + str(count))
