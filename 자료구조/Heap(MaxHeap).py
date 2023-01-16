class MaxHeap(object):
    def __init__(self):
        self.queue = []
    
    #값을 추가하는 함수
    def insert(self, n):
        #맨 마지막에 삽입할 값을 임의로 추가 
        self.queue.append(n)
        last_index = len(self.queue) -1    # 인덱스의 크기를 가져옴 
        while 0 <= last_index:    #인덱스 전부 확인할떄까지 확인
            parent_index = self.parent(last_index)  #부모의 인덱스를 가져옴
            if 0 <= parent_index and self.queue[parent_index] < self.queue[last_index]:  #부모의 인덱스가 0보다크고 부모인덱스 값보다 크다면 실행
                self.swap(last_index, parent_index)   # 자식인덱스와 부모인덱스를 바꿈
                last_index = parent_index       #자식인덱스에 부모인덱스를 넣음
            else:
                break
    
    #값을 삭제하는 함수
    def delete(self):
        last_index = len(self.queue) - 1    #마지막인덱스 가져옴
        if last_index < 0:     
            return -1 
        self.swap(0, last_index)   #큐는 선입선출이기떄문에 맨처음인덱스와 마지막인덱스 교체
        maxv = self.queue.pop()    #인덱스 삭제후 값을 넣음
        self.maxHeapify(0)   #root부터 재정렬
        print(maxv)
        return maxv

    #임시 root값부터 자식들과 값을 비교해가면서 재정렬하는 함수
    def maxHeapify(self, i):
        left_index = self.leftchild(i)  #부모의 왼쪽자식을 가져옴
        right_index = self.rightchild(i)  #부모의 오른쪽자식을 가져옴
        max_index = i       # 더 큰 값의 인덱스를 넣어주는 함수

        if left_index <= len(self.queue)-1 and self.queue[max_index] < self.queue[left_index]:  #왼쪽자식이 부모보다 값이 클떄 실행
            max_index = left_index
        if right_index <= len(self.queue)-1 and self.queue[max_index] < self.queue[right_index]: #오른쪽자식이 부모보다 값이 클때 실행
            max_index = right_index

        if max_index != i:   # 만약 자신이 가장 큰게 하니면 실행
            self.swap(i, max_index)   #부모와 자식 인덱스 교체
            self.maxHeapify(max_index)  # 재실행

    def leftchild(self, index):
        return index*2 + 1

    def rightchild(self, index):
        return index*2 + 2

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def parent(self, index):
        return (index -1) // 2


