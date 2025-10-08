class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
    
class DoublyLL:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def Append(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
    



dll = DoublyLL()


dll.insertAtEnd(10)
dll.insertAtEnd(20)
dll.insertAtEnd(30)


dll.Append(40)
dll.Append(50)

print("Forward Traversal:")
curr = dll.head
while curr:
    print(curr.val, end=" <-> ")
    curr = curr.next
print("None")


print("Backward Traversal:")
curr = dll.head
while curr and curr.next:   
    curr = curr.next
while curr:
    print(curr.val, end=" <-> ")
    curr = curr.prev
print("None")
