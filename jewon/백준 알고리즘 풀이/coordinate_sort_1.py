import sys
num = int(sys.stdin.readline())

Narr = []

for i in range(num):
    Narr.append(list(map(int,input().split(" "))))

Narr.sort(key=lambda x:(x[0],x[1]))

for i in Narr:
    print(i[0],i[1])