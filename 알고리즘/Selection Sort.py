list_a = [10,3,55,44,89,98,6]
min = 0  # 최소값의 인덱스 값을 넣을 함수 정의
temp = 0

for i in range(len(list_a)-1): #0 ~ 리스트 마지막까지
    min = i # 현재 인덱스값을 min에 넣음
    for j in range(i+1, len(list_a)):   # 현재위치 다음 인덱스부터 비교해서 제일 작은 인덱스 값을 넣는 작업
        if list_a[j] < list_a[min]:
            min = j
    temp = list_a[min]      
    list_a[min] = list_a[i]
    list_a[i] = temp          # 인덱스 값을 바꾸는 작업

print(list_a)