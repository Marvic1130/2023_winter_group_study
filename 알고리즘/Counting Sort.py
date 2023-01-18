#리스트 자료형(배열)을 활용한 계수 정렬
def counting_sort(arr):

    max_arr = max(arr)
    count = [0] * (max_arr+1)
    sorted_arr = list()

    for i in arr:
        count[i] += 1
    
    for i in range(max_arr+1):
        for __ in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr

#딕셔너리 자료형 활용
def counting_sort2(arr):
    count = dict()
    sorted_arr = list()

    for i in arr:
        if i in count:
            count[i] += 1
        else: 
            count[i] = 1
    
    for i in sorted(count.keys()):
        for __ in range(count[i]):
            sorted_arr.append(i)
    return sorted_arr