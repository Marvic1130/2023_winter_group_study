# 알고리즘 정의
# 안전 정렬 : 동일한 값에 기존 순서가 유지(버블,삽입)
# 불안정 정렬 : 동일한 값에 기존 순서가 유지되지 않음(선택,퀵)

# 퀵정렬은 최악의 경우 n^2, 평균적으로는 nlogn의 속도를 가진다.

# Processing
"""
1. 피벗선택
2. 오른쪽(j)에서 왼쪽으로 가면서 피벗보다 작은 수 찾는다.
3. 왼쪽(i)에서 오른쪽으로 가면서 피버보다 큰 수 찾는다.
4. 각 인덱스 i,j에 대한 요소를 교환
5. 2,3,4번 과정 반복
6. 더이상 2,3번 진행이 불가능하면, 현재 피벗과 교환
7. 이제 교환된 피벗 기준으로 왼쪽엔 피벗보다 작은 값, 오른쪽엔 큰 값들만 존재한다.
8. 작은 값 리스트와 큰 값리스트에 대해서 순차적으로 퀵정렬을 수행한다(재귀함수)
"""

# 기본 Quick sort code // 다시 이해 해서 만들기

# 리스트자료형의 변수 생성  
Narr = [9,4,6,2,1,5,3,7,8]

def Quick_sort(arr,left,right):
    if left >= right : return
    pi = partition(arr,left,right)

    Quick_sort(arr,left,pi-1)
    Quick_sort(arr,pi+1,right)

def partition(arr,left,right):
    pivot = arr[left]
    i = left, j = right

    while i < j:
        while pivot < arr[j]:
            j -= 1
        while i < j and pivot >= arr[i]:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[left] = arr[i]
    arr[i] = pivot

    return i



print(f"정렬 전 : {Narr}")
Quick_sort(Narr,Narr[0],Narr[8])
print(f"정렬 후 : {Narr}")

# 파이썬 특징을 활용한 Quick sort 
Narry = [9,4,6,2,1,5,3,7,8]


# 장점

# 단점

