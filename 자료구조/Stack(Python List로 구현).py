# Stack Class

class stack:
    # 스택 객체 생성
    def __init__(self):
        self.items = []

    #스택 요소 추가
    def push(self, item):
        self.items.append(item)
    
    #스택 맨 뒤 요소 삭제하고 리턴
    def pop(self):
        pop_object =None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            pop_object = self.items.pop()
        return pop_object

    #스택 맨 뒤(맨 위)에 요소 리턴
    def top(self):
        top_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.items[-1]
        return top_object

    #스택이 비었는지 확인(비었으면 True 리턴)
    def isEmpty(self):
        is_empty = False
        if len(self.items) == 0:
            is_empty = True
        return is_empty
