num = int(input())
Narr = []

for i in range(num):
    Narr.append(int(input()))

for i in range(num-1):
    for j in range(num - i - 1):
        if Narr[j] > Narr[j+1]:
            Narr[j],Narr[j+1] = Narr[j+1],Narr[j]

print(Narr)