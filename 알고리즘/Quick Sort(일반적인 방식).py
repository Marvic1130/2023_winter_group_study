list_a = [5,23,56,26,89,11,84,223,10]

# 퀵 정렬 정의
def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    
    pivot = start  # 피벗은 첫번쨰 원소로 지정 
    left = start + 1    # 왼쪽값은 피벗보다 큰 값을 찾는다 
    right = end         # 오른쪽값은 피벗보다 작은 값을 찾는다 

    #왼쪽이 오른쪽보다 작거나 같으면 계속 실행 
    while(left <= right):
        # 피벗보다 큰 값을 찾을 떄까지 반복 
        while(left <= right and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 값을 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        # 엇갈렸다면 작은 데이터와 피벗을 교체 
        if (left > right):
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[left], array[right] = array[right], array[left]

        # 분할 이후에 왼쪽 부분과 오른쪽 부분에서 각 정렬 수행 
        quick_sort(array, start, right -1)
        quick_sort(array, left, end)

quick_sort(list_a, 0, len(list_a)-1)
print(list_a)