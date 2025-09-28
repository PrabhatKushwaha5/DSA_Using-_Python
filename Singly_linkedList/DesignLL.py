class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
       
        self.head = Node(0)
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        node = Node(val)
        node.next = pred.next
        pred.next = node

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next



myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)       
myLinkedList.addAtTail(3)      
myLinkedList.addAtIndex(1, 2)   
print(myLinkedList.get(1))      
myLinkedList.deleteAtIndex(1)  
print(myLinkedList.get(1))