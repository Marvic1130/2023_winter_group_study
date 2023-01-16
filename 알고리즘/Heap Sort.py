arr = [99,11,22,33,67,77]
def heap_sort(arr):
    n = len(arr)
    #heap 구성
    for i in range(n):
        c = i
        while c != 0:
            r = (c-1)//2  #부모 인덱스를 지정
            if arr[r] < arr[c]:   #자식이 부모값보다 클떄 
                arr[r], arr[c] = arr[c], arr[r]   #서로 값을 바꾼다
            c = r
    #크기를 줄여가면서 heap 구성
    for j in range(n-1, -1,- 1):
        arr[0], arr[j] = arr[j], arr[0]  # 
        r = 0
        c = 1
        while c < j:
            c = r*2 +1    #자식 인덱스 지정
            if c < j-1 and arr[c] < arr[c+1]:   #자식중에 큰 값을 찾기
                c += 1 
            if c < j and arr[r] < arr[c]:  # 자식이 부모보다 값이 크다면 서로 바꿈
                arr[r], arr[c] = arr[c], arr[r]
            r = c
    print(arr)

heap_sort(arr)