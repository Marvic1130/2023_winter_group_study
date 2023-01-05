list_a = [10,3,55,44,89,98,6]
temp = 0       # 임시로 해당위치 값을 저장하는 함수
prev = 0       

for i in range(1,len(list_a)):
    temp = list_a[i]
    prev = i-1      #해당 위치 이전 위치를 지정 
    while prev >=0 and list_a[prev] > temp:  # prev가 0보다 크고 비교하는 함수의 값이 해당위치 값보다 클떄 실행
        list_a[prev+1] = list_a[prev]     # 큰 값들을 뒤로 밀어내는 작업
        prev -= 1                         
    list_a[prev+1] = temp               # prev가 temp값보다 작은 값중에 제일 큰값 위치를 가리키는 중
                                        #prev+1에 temp값을 넣어주면 된다

print(list_a)