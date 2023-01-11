import sys

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
        # print(arr)
    sort(arr)
    return arr

num = int(sys.stdin.readline())        #입력받을 숫자 갯수
list_a = []

for i in range(num):
    number = int(sys.stdin.readline())
    list_a.append(number) # 숫자들을 입력하여 리스트안에 넣음(int형 변환)

result = merge_sort(list_a)

for i in result:      #리스트안에 요소들을 출력 
    print(i)






# ------------------------------------------------
# import sys

# num = int(sys.stdin.readline())        #입력받을 숫자 갯수        
# list_a = []                            # sys.stdin.readline() 한 줄에 여러개의 숫자를 입력받겠다.

# for i in range(num):
#     number = int(sys.stdin.readline())
#     list_a.append(number) # 숫자들을 입력하여 리스트안에 넣음(int형 변환)

# result = sorted(list_a)

# for i in result:      #리스트안에 요소들을 출력 
#     print(i)
