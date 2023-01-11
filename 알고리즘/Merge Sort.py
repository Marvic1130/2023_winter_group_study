list_a = [5,23,56,26,89,11,84,223,10]

def merge_sort(arr):
    def sort(unsorted_list):
        if len(unsorted_list) <= 1 :
            return 
        # 두개의 리스트로 분할, 아래에서 재귀적으로 실행 
        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right)

    def merge(left, right):
        i = 0
        j = 0
        k = 0

        #두 분할된 리스트를 비교해서 작은 순서대로 리스트에 삽입
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1

        #나머지 값들을 리스트에 삽입
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        print(arr)
    sort(arr)

merge_sort(list_a)
print(list_a)