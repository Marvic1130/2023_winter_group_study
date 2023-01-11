import sys

num = int(sys.stdin.readline().rstrip())        #입력받을 숫자 갯수
list_a = [0] * 10001                            # sys.stdin.readline().rstrip()   한줄에 여러개의 문자를 입력받는데 오른쪽 공백을 지움

for i in range(num):
    number = int(sys.stdin.readline().rstrip())
    list_a[number] += 1 # 숫자들을 입력하여 리스트안에 넣음(int형 변환)

result = sorted(list_a)

for i in range(1, 10001):      #리스트안에 요소들을 출력 
    if list_a[i] != 0:
        for i in range(list_a[i]):
            print(i)
