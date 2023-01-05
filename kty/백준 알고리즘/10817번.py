a,b,c = map(int, input().split())
list_a = [a,b,c]
min = 0
temp = 0

for i in range(len(list_a)-1):
    min = i
    for j in range(i+1, len(list_a)):
        if list_a[j] < list_a[min]:
            min = j
    temp = list_a[min]
    list_a[min] = list_a[i]
    list_a[i] = temp

print(list_a[1])