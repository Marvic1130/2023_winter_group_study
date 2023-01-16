num = int(input())
Narr = []

#입력받는 반복문
for i in range(num):
    Narr.append(int(input()))   #append로 배열에 추가하는 방식

#버블정렬 알고리즘
for i in range(num-1):
    for j in range(num - i - 1):
        if Narr[j] > Narr[j+1]:     #인덱스 값이 다음 인덱스값 보다 크다면
            Narr[j],Narr[j+1] = Narr[j+1],Narr[j]

#출력문
print(Narr)