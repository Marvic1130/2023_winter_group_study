def Average(arr):
    num = 0
    for i in range(5):
        num += list_a[i]
    return print(int(num / 5)) 

def median_value(arr):
    result = sorted(arr)
    print(result[2])

list_a = []
for i in range(5):
    list_a.append(int(input()))

Average(list_a)
median_value(list_a)

