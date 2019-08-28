class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr
    
    

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s



    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

# 여기부터가 과제입니다

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        # 삭제하려는 node가 첫번째 node인 경우
        if pos == 1:
            curr = self.getAt(1)
            self.head = self.getAt(pos+1)
            # 삭제하려는 node가 유일 node인 경우
            if self.nodeCount == 1:
                self.tail = None
        # 삭제하려는 node가 마지막 node인 경우
        elif pos == self.nodeCount:
            curr = self.getAt(pos)
            self.tail = self.getAt(pos-1)
            self.tail.next = None
        else:
            prev = self.getAt(pos-1)
            curr = self.getAt(pos)
            prev.next = curr.next
        self.nodeCount = self.nodeCount - 1
        return curr.data
        
refac
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        # 삭제하려는 node가 첫번째 node인 경우
        if pos == 1:
            curr = self.getAt(1)
            self.head = curr.next
            # 삭제하려는 node가 유일 node인 경우
            if self.nodeCount == 1:
                self.tail = None
        else:
            prev = self.getAt(pos-1)
            curr = self.getAt(pos)
            prev.next = curr.next
            # 삭제하려는 node가 마지막 node인 경우
            if pos == self.nodeCount:
                self.tail = prev
        self.nodeCount = self.nodeCount - 1
        return curr.data
        

def solution(x):
    return 0
    
# interactive shell 연습용
a = Node(1)
b = Node(23)
c = Node(1253)
d = Node(2)

L = LinkedList()
L.insertAt(1, a)
L.insertAt(2, b)
L.insertAt(3, c)
L.insertAt(4, d)
