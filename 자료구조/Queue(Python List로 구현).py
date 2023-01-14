class Queue():
    def __init__(self):
        self.queue = []

    #큐 객체 생성
    def enqueue(self, data):
        self.queue.append(data)  # append를 활용하여 구현 
    
    #큐 객체 삭제 
    def dequeue(self):
        dequeue_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            dequeue_object = self.queue[0]   #첫번쨰 값을 가져오고
            self.queue = self.queue[1:]     # 나머지 값들을 저장
        return dequeue_object

    #큐 맨 앞에 요소 리턴
    def peek(self):
        peek_object = None
        if self.isEmpty():
            print("Queue is Empty")
        else:
            peek_object = self.queue[0]
        return peek_object
    
    #큐가 비어있는지 확인(비어있으면 True리턴)
    def isEmpty(self):
        is_empty = False
        if len(self.queue) == 0:
            is_empty = True
        return is_empty
