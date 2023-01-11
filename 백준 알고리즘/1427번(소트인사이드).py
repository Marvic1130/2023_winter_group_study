num = int(input())
list_a = []
sum = 0

while(num != 0):
    list_a.append(num%10)
    num = num//10

result = sorted(list_a)

for i in reversed(result):
    sum += i
    sum *= 10
    
print(sum//10)

