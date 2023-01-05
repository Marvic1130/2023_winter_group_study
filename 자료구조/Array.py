#왼쪽으로 한번 회전
def leftRotate_one(list_a = []):
    temp = list_a[0]
    for i in range(len(list_a)-1):
        list_a[i] = list_a[i+1]
    list_a[i] = temp

# 왼쪽으로 d만큼 회전
def leftRotate(d,n, list_a = []):
    for i in range(d):
        leftRotate_one(list_a)

def printArray(list_a = []):
    for i in range(len(list_a)):
        print(list_a[i])



list_a = [10,3,4,5,6,123,5]

leftRotate_one(list_a)

printArray(list_a)