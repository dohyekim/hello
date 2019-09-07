class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result



    def reverse(self):
        result = []
        curr = self.tail.prev
        i = 1
        while (i <= self.nodeCount):
            result.append(curr.data)
            curr = curr.prev
            i += 1
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertBefore(self, next, newNode):
        prev = next.prev
        newNode.next = next
        newNode.prev = prev
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def __repr__(self):
        
        if self.nodeCount == 0:
            return "Empty"
        
        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' => '
            curr = curr.next
        return s

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        next = prev.next
        prev.next = next.next
        next.next.prev = prev
        self.nodeCount -= 1
        return next.data

    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail
        self.nodeCount += L.nodeCount
        return self
        
    def popBefore(self, next):
        prev = next.prev
        next.prev = prev.prev
        prev.prev.next = next
        self.nodeCount -= 1
        return prev.data        


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        curr = self.getAt(pos)
        prev = curr.prev
        self.popAfter(prev)
        return curr.data

def solution(x):
    return 0


# interactive shell에서 연습용
a = Node(24)
b = Node(36)
c = Node(72)
d = Node(84)
L = DoublyLinkedList()
L.insertAt(1,a)
L.insertAt(2,b)
L.insertAt(3,c)
L.insertAt(4, d)

L2 = DoublyLinkedList()
L2.insertAt(1, Node(1))
L2.insertAt(2, Node(2))
L2.insertAt(3, Node(3))
L2.insertAt(4, Node(4))

L3 = DoublyLinkedList()