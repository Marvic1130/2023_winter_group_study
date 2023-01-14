# LinkedList를 만들기 위해 필요한 Node 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack():
    def __init__(self):
        self.head = None

    #새로운 데이터를 감은 노드를 생성
    def push(self, data):
        new_node = Node(data)   #새로운 데이터를 담은 노드 먼저 생성
        new_node.next = self.head # 생성한 이후 노드의 next에 리스트의 head를 연결
        self.head = new_node #self.head에 새로운 데이터를 담은 노드 연결
    
    #데이터 담은 노드 삭제 
    def pop(self):
        pop_object = None
        if self.isEmpty(): #isEmpty 메소드를 통해 스택이 비어있는지 확인
            print("Stack is Empty")
        else:
            pop_object = self.head.data # head데이터를 꺼냄
            self.head = self.head.next #head에 self의 next 노드를 넣어주고 꺼낸 데이터 return 
        return pop_object
    
    #스택 맨 뒤(맨 위)에 있는 노드 데이터를 리턴
    def top(self):
        top_object = None 
        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.head.data   #head노드의 데이터를 꺼내와 return 
        return top_object

    #스택이 비어있는지 확인
    def isEmpty(self):
        is_empty = False
        if self.head is None:
            is_empty = True
        return is_empty
