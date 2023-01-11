def minimum(arr):
    result = 0
    arr_min = sorted(arr)
    for i in range(len(arr)+1):
        result += sum(arr_min[0:i])    
    print(result)

person = int(input())
arr = list(map(int, input().split()))   

minimum(arr)