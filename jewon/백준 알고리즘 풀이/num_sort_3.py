import sys

num = int(sys.stdin.readline())
Narr = [0] * 10001

for i in range(num):
    Narr[int(sys.stdin.readline())] +=1

for i in range(10001):
    if Narr[i] != 0:
        for j in range(Narr[i]):
            print(i)