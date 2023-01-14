#LinkedList를 만들기 위해 필요한 Node정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue():
    #front와 rear를 먼저 None으로 init
    def __init__(self):
        self.front = None
        self.rear = None
    #새로운 데이터를 담은 노드를 생성
    def enqueue(self, data):
        new_node= Node(data) #노드를 먼저 생성

        if self.front is None: # front가 None이면 front와 rear에 먼저 데이터 생성
            self.front = new_node
            self.rear = new_node
        else:                   # 그렇지 않다면 rear의 next에 새로운 데이터를 넣고
            self.rear.next = new_node # 이를 다시 rear에 넣는다
            self.rear = self.rear.next
    #데이터를 담은 노드를 삭제
    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():   #먼저 Queue가 비어있는지 확인
            print("Queue is Empty")
        else:                #front의 노드에서 데이터를 꺼내온뒤 front에 front의 next노드를 넣어주고 
            dequeue_object = self.front.data  #아까 꺼낸 데이터를 return
            self.front = self.front.next

        if self.front is None:    # 
            self.rear = None
        return dequeue_object
    #큐 맨 앞에 있는 노드 데이터를 리턴
    def peek(self):
        front_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            front_object = self.front.data
        return front_object
    #큐가 비어있는지 확인(비어있다면 True리턴)
    def isEmpty(self):
        is_empty = False
        if self.front is None:
            is_empty = True
        return is_empty