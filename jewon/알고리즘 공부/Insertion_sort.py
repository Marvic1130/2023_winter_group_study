# 알고리즘 정의
# 손의 카드를 정렬하는 방법과 유사하다.
# Selection 정렬과 유사하지만 좀 더 효율적인 정렬 알고리즘 이다.
# 2번째 원소부터 시작하여 그 앞(왼쪽)의 원소들과 비교하여 삽입할 위치를 지정한 후, (이어서..)
# 원소를 뒤로 옮기고 지정된 자리에 자료를 삽입하여 정렬하는 알고리즘

# Process(Ascending)
"""
1. 정렬은 2번째 위치(index)의 값을 temp에 저장한다.
2. temp와 이전에 있는 원소들과 비교하며 삽입해나간다.
3. '1'번으로 돌아가 위치(index)의 값을 temp에 저장하고, 반복한다.
"""

# code
# 리스트자료형의 변수 생성
Narr = [9,4,6,2,1,5,3,7,8]

# 삽입정렬을 수행할 함수 정의
def Insertion_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        prev = i - 1
        while (prev >= 0) and (arr[prev] > temp) :
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = temp
            

# 출력결과
print(f"정렬 전 : {Narr}")
Insertion_sort(Narr)
print(f"정렬 후 : {Narr}")

# 장점
"""
1. 알고리즘이 단순하다.
2. 대두분의 원소가 이미 정렬되어 있는 경우 매우 효율적일수 있다.
3. 정렬하고자 하는 배열 안에서 교환하는 방식이므로, 다른 메로리 공간을 필요로 하지 않는다. ==> 제자리정렬
4. 안정 정렬(Stable Sort)입니다.
5. Selection 정렬 Bubble 정렬 같은 n^2 알고리즘에 비교하여 상대적으로 빠르다.
"""

# 단점
"""
1. 평균과 최악의 시간복잡도가 n^2으로 비효율적이다.
2. Bubble정렬과, Selection 정렬과 마찬가지로, 배열의 길이가 길어질수록 비효율적이다.
"""