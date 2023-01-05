class Node:
    # 클래스 정의
    def __init__(self, data =0, next=None): 
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # 해더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):   
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(data)

    # 모든 노드 값 출력
    def print_all(self):     
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

    #노드 인덱스 알아내기 
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    #노드 중간에 새로운 값을 삽입하는 방법
    def add_node(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    #노드 안에 값을 삭제하는 방법
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index-1)
        node.next = node.next.next


sl = LinkedList(100)
sl.append(400)
sl.add_node(1, 200)
sl.delete_node(2)

sl.print_all()
# def printNodes(node):
#     crnt_node = node
#     while crnt_node != None:
#         print(crnt_node.data, end= " ")
#         crnt_node = crnt_node.next

# class SLinkedList:
#     def __init__(self):
#         self.head = None

#     def addHead(self, data):
#         node = ListNode(data)
#         node.next = self.head
#         self.head = node
    
#     def addBack(self, data):
#         node = ListNode(data)
#         crnt_node = self.head
#         while crnt_node.next:
#             crnt_node = crnt_node.next
#         crnt_node.next = node

#     def findNode(self, data):
#         crnt_node = self.head
#         while crnt_node != None:
#             if crnt_node.data == data:
#                 return crnt_node
#             crnt_node = crnt_node.next

#     def addAfter(self, node, data):
#         new_node = ListNode(data)
#         new_node.next = node.next
#         node.next = new_node

#     def deleteAfter(self, prev_node):
#         if prev_node.next != None:
#             prev_node.next = prev_node.next.next
