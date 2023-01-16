# 알고리즘 정의
# Bubble sort와 유사한 알고리즘으로, 해당 순서에 원소를 넣을 위치는 이미 정해져 있고, 어떤 원소를 넣을지 선택하는 알고리즘
# Selection sort는 배열에서 해당 자리를 선택하고 그자리에 오는 값을 찾는 방법

# Processing
"""
1. 주어진 배열 중에 최소값을 찾는다.
2. 그값을 맨뒤에 위치한 값과 교체한다.
3. 맨 처음 위치를 뺀 나머지 배열을 같은 방법으로 교체한다.
"""

# code
# 리스트자료형의 변수 생성
Narr = [9,4,6,2,1,5,3,7,8]

# 선택정렬을 수행할 함수정의
def Selection_sort(arr):
    for i in range(len(arr)):
        index_min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[index_min]:
                index_min = j

        arr[i], arr[index_min] = arr[index_min],arr[i]

# 출력결과
print(f"정렬 전 : {Narr}")
Selection_sort(Narr)
print(f"정렬 후 : {Narr}")

# 장점
"""
1. Bubble 정렬과 마찬가지로 단순한 알고리즘이다.
2. 정렬을 위한 비교 횟수는 많지만, Bubble 정렬에 비해 실제 교환되는 횟수는 적기 떄문에
   많은 교환이 일어나야하는 자료상태에서는 비교적 효율적이다.
3. Bubble 정렬과 마찬가지로 정렬하고자 하는 배열안에서 교환하는 방식이므로, 다른 메모리를 필요로 하지 않는다. 제자리 정렬(in-place sorting)
"""

# 단점
"""
1. 시간복잡도가 비효율적이다.
2. 불안정 정렬이다. *불안정 정렬은 중복된값이 입력순서와 동일하지 않게 정렬되는 알고리즘을 말한다.
"""