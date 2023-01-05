# list_a = [99,10,55,92,45,67,3,2]
# temp = 0

# for i in range(len(list_a)-1):
#     for j in range(len(list_a)-(i+1)):
#         if list_a[j] > list_a[j+1]:
#             temp = list_a[j]
#             list_a[j] = list_a[j+1]
#             list_a[j+1] = temp
#         else:
#             continue


# print(list_a)

num = int(input())        #입력받을 숫자 갯수
list_a = []
temp = 0

for i in range(num):
    list_a.append(int(input()))     # 숫자들을 입력하여 리스트안에 넣음(int형 변환)
    
for i in range(len(list_a)-1):      # 숫자들을 비교하여서 오른차순으로 정렬
    for j in range(len(list_a)-(i+1)):
        if list_a[j] > list_a[j+1]:
            temp = list_a[j]
            list_a[j] = list_a[j+1]
            list_a[j+1] = temp

#print(list_a)

for i in range(len(list_a)):      #리스트안에 요소들을 출력 
    print(list_a[i])
