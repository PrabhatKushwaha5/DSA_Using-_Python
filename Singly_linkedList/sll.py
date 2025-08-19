class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    def Append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        
    def traversal(self):
        if not self.head:
            print("Empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr = curr.next
            print()
    
sll = SLL()
sll.Append(10)
sll.Append(20)
sll.Append(30)
sll.traversal()
