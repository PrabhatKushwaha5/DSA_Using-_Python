class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    # Add element at end
    def Append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        
    # Traverse and print list
    def traversal(self):
        if not self.head:
            print("Empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next
            print()
    
    # Insert at given position
    def insert_at(self, val, position):
        new_node = Node(val)   
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev_node = None
            count = 0
            while curr is not None and count < position:
                prev_node = curr
                curr = curr.next
                count += 1
            if prev_node is None:   # list was empty
                self.head = new_node
            else:
                prev_node.next = new_node
                new_node.next = curr
    
    # Delete by value
    def delete(self, val):
        if self.head is None:   # empty list
            print("List is empty")
            return
        
        temp = self.head
        
        # Case 1: delete head
        if temp.val == val:
            self.head = temp.next
            temp = None
            return
        
        # Case 2: delete non-head node
        prev = None
        while temp is not None:
            if temp.val == val:
                prev.next = temp.next
                temp = None
                return
            prev = temp
            temp = temp.next
        
        print(f"Value {val} not found in list")


sll = SLL()
sll.Append(10)
sll.Append(20)
sll.Append(30)
sll.traversal()         
sll.insert_at(40, 2)
sll.traversal()          
sll.delete(20)
sll.traversal()          
sll.delete(10)
sll.traversal()          
sll.delete(100)         
